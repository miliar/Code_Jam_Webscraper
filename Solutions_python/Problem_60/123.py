import math, sys

class InputError(Exception):
    pass


class Input(object):
    def __init__(self, input_stream):
        self.input_stream = input_stream
        self.__line_words = []
        self.__next_word = None
        self.__num_words = 0
    def _get_line(self):
        return self.input_stream.readline().strip()
    def get_line(self):
        self.__line_words = self._get_line().split()
        self.__num_words = len(self.__line_words)
        self.__next_word = 0

    def read_word(self):
        if self.__next_word == None:
            raise InputError("No words left on the current line")
        word = self.__line_words[self.__next_word]
        self.__next_word += 1
        if self.__next_word >= self.__num_words:
            self.__next_word = None
        return word

    def read_line_list(self, ltype):
        if self.__next_word == None:
            self.get_line()
        result = []
        while True:
            try:
                result.append(ltype(self.read_word()))
            except InputError:
                break
        return result

    def read_line(self, *args):
        if self.__next_word == None:
            self.get_line()
        a = 0
        result = []
        while True:
            try:
                result.append(args[a](self.read_word()))
                if a + 1 < len(args): a += 1
            except InputError:
                break
        if len(result) == 1:
            return result[0]
        return result

    def read_line_into_container(self, container, atype):
        while True:
            try:
                container.append(atype(self.read_word()))
            except InputError:
                break

class Chick(object):
    def __init__(self, x, v):
        self.x = x
        self.v = v

class TestCase(object):
    def __init__(self, input):
        self.N, self.K, self.B, self.T = input.read_line(int, int, int, int)
        X = input.read_line_list(int)
        V = input.read_line_list(int)
        self.chicks = [Chick(X[i], V[i]) for i in range(self.N)]
        fgroup = []
        if self.K == 0:
            self.result = "0"
            return
        for i in range(self.N):
            if self.can_reach_barn(self.chicks[i]):
                fgroup.append(i)
        # only worry about the first K chicks that can make it to the barn
        if len(fgroup)< self.K:
            self.result = "IMPOSSIBLE"
            return
        fgroup.reverse()
        fgroup = fgroup[0:self.K]
        fgroup.reverse()
        fa = fgroup[0]
        swaps = 0
        for i in range(fa, self.N):
            if i not in fgroup:
                swaps += len([f for f in fgroup if f<i])
        self.result = str(swaps)
    def can_reach_barn(self, chick):
        d = self.B - chick.x
        return d <= self.T*chick.v




def main():
    input = Input(sys.stdin)
    N = input.read_line(int)
    for n in range(1, N+1):
        sys.stderr.write("case #%d/%d\n"%(n,N))
        case = TestCase(input)
        sys.stdout.write("Case #%d: %s\n"%(n, case.result))

main()








