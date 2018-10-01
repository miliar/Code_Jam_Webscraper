class Solution(object):
    def __init__(self):
        self._test_cases = self._read_int()

    def solve(self):
        for case_index in range(1, self._test_cases + 1):
            test_input = self._read_input_for_single_test_case()
            result = self._solve_single_test_case(test_input)
            self._process_single_test_case_output(case_index, result)

    def _read_input_for_single_test_case(self):
        C, J = self._read_int_array()
        cameron = [self._read_int_array() for _ in xrange(C)]
        jamie = [self._read_int_array() for _ in xrange(J)]
        return sorted(cameron, key=lambda x: x[0]), sorted(jamie, key=lambda x: x[0])

    def _solve_single_test_case(self, test_input):
        cameron, jamie = test_input
        left_c = 720
        left_j = 720
        time = []
        for cam in cameron:
            time.append([cam[0], cam[1], 'J'])
            left_j -= cam[1] - cam[0]
        for jam in jamie:
            time.append([jam[0], jam[1], 'C'])
            left_c -= jam[1] - jam[0]
        time = sorted(time, key=lambda t: t[0])
        # if len(time) > 1:
        time.append([time[0][0] + 60 * 24, time[0][1] + 60 * 24, time[0][2]])
        candidates = []
        other = []
        for i in xrange(len(time) - 1):
            # if time[(i + 1) % len(time)][2] == time[i][2]:
            if time[i + 1][2] == time[i][2]:
                # candidates.append([(time[(i + 1) % len(time)][0] + 60 * 24 - time[i][1]) % (60 * 24), time[i][2]])
                candidates.append([(time[i + 1][0] + 60 * 24 - time[i][1]) % (60 * 24), time[i][2]])
            else:
                other.append((time[i + 1][0] + 60 * 24 - time[i][1]) % (60 * 24))
        candidates_jamie = sorted(filter(lambda x: x[1] == 'J', candidates), key=lambda x: x[0])
        candidates_cameron = sorted(filter(lambda x: x[1] == 'C', candidates), key=lambda x: x[0])
        can_j = 0
        while can_j < len(candidates_jamie):
            if candidates_jamie[can_j][0] <= left_j:
                left_j -= candidates_jamie[can_j][0]
                can_j += 1
            else:
                break
        can_c = 0
        while can_c < len(candidates_cameron):
            if candidates_cameron[can_c][0] <= left_c:
                left_c -= candidates_cameron[can_c][0]
                can_c += 1
            else:
                break
        return 2*(len(candidates_jamie) - can_j +len(candidates_cameron) - can_c) + len(other)

    @staticmethod
    def _process_single_test_case_output(case_index, result):
        print('Case #{}: {}'.format(case_index, result))

    @staticmethod
    def _read_int():
        return int(raw_input().strip())

    @staticmethod
    def _read_int_array():
        return map(int, raw_input().strip().split())

    @staticmethod
    def _read_string():
        return raw_input().strip()

    @staticmethod
    def _read_string_array():
        return raw_input().strip().split()


solution = Solution()
solution.solve()
