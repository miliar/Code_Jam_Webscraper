from codejam import CodeJamParser


IMPOSSIBLE = 'IMPOSSIBLE'

def solve_lms(i_l, i_m, i_s):
    l = i_l
    m = i_m
    s = i_s
    entries = [0, 1, 2] * s

    l -= s
    m -= s
    s = 0

    while m > 0:
        entries.insert(0, 1)
        entries.insert(0, 0)
        m -= 1
        l -= 1

    while l > 0:
        found = False
        for i in range(len(entries)-1):
            if entries[i] == 1 and entries[i+1] == 2:
                entries.insert(i+1, 0)
                l -= 1
                found = True
                break
        if not found:
            return None

    return entries


class Unicorns(CodeJamParser):
    """
    2017, Round 1B, B
    https://code.google.com/codejam/contest/3264486/dashboard
    """
    def get_cases(self):
        cases = int(next(self.source))
        for i in range(1, cases + 1):
            [n_str, r_str, o_str, y_str, g_str, b_str, v_str] = next(self.source).split(' ')
            yield (int(r_str), int(o_str), int(y_str), int(g_str), int(b_str), int(v_str))

    def handle_case(self, R, O, Y, G, B, V):
        # Pair G with R's
        if G == R and Y == O == B == V == 0:
            return 'RG' * G
        if G >= R and G != 0:
            return IMPOSSIBLE
        R_frags = ['RG' * G + 'R']  + ['R'] * (R - G - 1)
        if R == 0:
            R_frags = []

        # Pair V with Y's
        if V == Y and B == G == R == O == 0:
            return 'VY' * V
        if V >= Y and V != 0:
            return IMPOSSIBLE
        Y_frags = ['YV' * V + 'Y']  + ['Y'] * (Y - V - 1)
        if Y == 0:
            Y_frags = []

        # Pair O with B's
        if O == B and Y == G == R == V == 0:
            return 'OB' * O
        if O >= B and O != 0:
            return IMPOSSIBLE
        B_frags = ['BO' * O + 'B']  + ['B'] * (B - O - 1)
        if B == 0:
            B_frags = []

        matched = []

        r = len(R_frags)
        y = len(Y_frags)
        b = len(B_frags)
        if r >= y and r >= b:
            largest = R_frags
            middle, smallest = (
                (Y_frags, B_frags)
                if y >= b
                else (B_frags, Y_frags)
            )
        elif y >= b and y >= r:
            largest = Y_frags
            middle, smallest = (
                (B_frags, R_frags)
                if b >= r
                else (R_frags, B_frags)
            )
        elif b >= r and b >= y:
            largest = B_frags
            middle, smallest = (
                (R_frags, Y_frags)
                if r >= y
                else (Y_frags, R_frags)
            )

        l = len(largest)
        m = len(middle)
        s = len(smallest)

        solved_lms = solve_lms(l, m, s)
        if not solved_lms:
            return IMPOSSIBLE

        for i in solved_lms:
            if i == 0:
                matched.append(largest.pop())
            elif i == 1:
                matched.append(middle.pop())
            elif i == 2:
                matched.append(smallest.pop())

        return ''.join(matched)


if __name__ == '__main__':
    Unicorns()