class Case:

    def __init__(self, s, k=0, case_num=-1):
        self.s = s
        self.k = k
        self.case_num = case_num
        self.count = 0
        self.result = ''


    def start_flipping(self):

        # self.count <= len(self.s) retarded condition
        while not self._check_success() and self.count <= len(self.s):
            l_ind = 0
            r_ind = len(self.s) - 1
            flipped = False

            while not flipped:
                # print(self.s, self.k, self.case_num, self.count)
                if self.s[l_ind] == '-':
                    ind_changed = False
                    if l_ind + self.k <= len(self.s):
                        self._flip(l_ind)
                        flipped = True
                else:
                    l_ind += 1
                    ind_changed = True

                if flipped:
                    break

                if self.s[r_ind] == '-':
                    if r_ind - self.k >= -1:
                        self._flip(r_ind - self.k + 1)
                        flipped = True
                else:
                    r_ind -= 1
                    ind_changed = True

                # in case of (['+', '-', '+'], 3, 13)
                if not ind_changed:
                    # sorre
                    self.count = 100500
                    flipped = True


        if self.count > len(self.s):
            self.result = 'IMPOSSIBLE'

        else:
            self.result = str(self.count)


    def _check_success(self):
        if str(self.s).find('-') == -1:
            return True


    def _flip(self, index):
        self.count += 1
        for i in xrange(index, index + self.k):
            self._change(i)



    def _change(self, index):
        if self.s[index] == '-':
            self.s[index] = '+'
        else:
            self.s[index] = '-'

    def get_output(self):
        #Case #1: 3
        return 'Case #' + str(self.case_num) + ': ' + self.result + '\n'





