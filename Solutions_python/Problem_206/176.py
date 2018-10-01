from codejam import CodeJamParser


class Steed(CodeJamParser):
    """
    2017, Round 1B, A
    https://code.google.com/codejam/contest/3264486/dashboard
    """
    def get_cases(self):
        cases = int(next(self.source))
        for i in range(1, cases + 1):
            dest_str, N_str = next(self.source).split(' ')
            dest = int(dest_str)
            N = int(N_str)
            horses = []
            for i in range(N):
                k_str, s_str = next(self.source).split(' ')
                horses.append((int(k_str), int(s_str)))
            yield dest, horses,

    def handle_case(self, dest, horses):
        N = len(horses)
        # print (N, dest, horses)
        longest_time = 0
        for horse in horses:
            init, speed = horse
            time_to_reach_dest = (dest - init) / speed
            if time_to_reach_dest > longest_time:
                longest_time = time_to_reach_dest
        return '%.6f' % (dest / longest_time)

if __name__ == '__main__':
    Steed()