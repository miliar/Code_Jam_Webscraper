# -*-coding:utf-8 -*

# import math
# from operator import itemgetter
# from fractions import Fraction
# from functools import lru_cache

def check(suite, R, Y, B):

    if len([1 for c in suite if c == 'R']) != R:
        print('real R:', R, 'given:', len([1 for c in suite if c == 'R']))
        return False

    if len([1 for c in suite if c == 'B']) != B:
        # print({'R': R, 'Y': Y, 'B': B})
        # print(suite)
        # exit(0)
        print('real B:', B, 'given:', len([1 for c in suite if c == 'B']))
        return False

    if len([1 for c in suite if c == 'Y']) != Y:
        print('real Y:', Y, 'given:', len([1 for c in suite if c == 'Y']))
        return False

    n = len(suite)
    for i in range(n):
        if suite[i] == suite[(i+1)%n]:
            return False

    return True


def main_func(N, R, O, Y, G, B, V):
    if O == 0 and G == 0 and V == 0:
        maxi = max(R, Y, B)
        if maxi > N/2:
            return 'IMPOSSIBLE'
        else:
            if R >= Y >= B:
                r, y, b = ('R', 'Y', 'B')
            elif R >= B >= Y:
                r, y, b = ('R', 'B', 'Y')
            elif Y >= R >= B:
                r, y, b = ('Y', 'R', 'B')
            elif Y >= B >= R:
                r, y, b = ('Y', 'B', 'R')
            elif B >= R >= Y:
                r, y, b = ('B', 'R', 'Y')
            else:
                r, y, b = ('B', 'Y', 'R')

            n_r, n_y, n_b = tuple(sorted([R, Y, B], reverse=True))
            nb_color = {
                r: n_r,
                y: n_y,
                b: n_b
            }
            # print(nb_color)
            result = ''
            next_color = r

            while nb_color[r] > 0 and nb_color[y] > 0 and nb_color[b] > 0:
                result += next_color
                nb_color[next_color] -= 1

                if next_color == r:
                    if nb_color[y] > nb_color[b]:
                        next_color = y
                    else:
                        next_color = b
                elif next_color == y or next_color == b:
                    next_color = r

            if nb_color[r] >= nb_color[y] >= nb_color[b]:
                r_bis, y_bis, b_bis = (r, y, b)
            elif nb_color[r] >= nb_color[b] >= nb_color[y]:
                r_bis, y_bis, b_bis = (r, b, y)
            elif nb_color[y] >= nb_color[r] >= nb_color[b]:
                r_bis, y_bis, b_bis = (y, r, b)
            elif nb_color[y] >= nb_color[b] >= nb_color[r]:
                r_bis, y_bis, b_bis = (y, b, r)
            elif nb_color[b] >= nb_color[r] >= nb_color[y]:
                r_bis, y_bis, b_bis = (b, r, y)
            else:
                r_bis, y_bis, b_bis = (b, y, r)

            next_color = r_bis
            while nb_color[r_bis] > 0 and nb_color[y_bis] > 0:
                result += next_color
                nb_color[next_color] -= 1

                if next_color == r_bis:
                    next_color = y_bis
                else:
                    next_color = r_bis

            result += nb_color[r_bis]*r_bis
            result += nb_color[y_bis]*y_bis

            if check(result, R, Y, B):
                # print('HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH')
                return result
            else:
                return 'IMPOSSIBLE'


# print(main_func())

# ------------------------------------------------------------------------------------------------------------------------------
# We apply mainFunc to each input
# ------------------------------------------------------------------------------------------------------------------------------

hl = 1  # "Header lines" :Number of lines at the beginning of the input file (header information)
lpc = 1  # "Lines per test case" number of lines for each entry of input
# (lpc will be used only if that number is the same for every case)
lineSep = "\n"  # Line separator
colSep = " "  # column separator

with open("input.txt", 'r') as inputFile:
    # ------------------------------------------------------------------------------------------------------------
    # Parsing the input
    # ------------------------------------------------------------------------------------------------------------
    # ------------------------------------------------------------------------
    # Parsing the header
    # ------------------------------------------------------------------------
    inputLines = inputFile.read().split(lineSep)
    while inputLines[-1] == '': del inputLines[-1]  # Deleting all empty lines at the end
    T = int(inputLines[0])  # Number of test cases
    # ------------------------------------------------------------------------

    # ------------------------------------------------------------------------
    # Parsing the body
    # ------------------------------------------------------------------------
    caseStartIndex = [hl]
    for i in range(T):  # caseStartIndex[T] = 1 + index of the last line
        # (ie : the index where would start case T+1 if it existed). In most cases we won't use it.
        nbLinesForThisCase = lpc
        # nbLinesForThisCase = int(inputLines[caseStartIndex[i]]) + 1
        caseStartIndex.append(caseStartIndex[i] + nbLinesForThisCase)
    # ------------------------------------------------------------------------

    # ------------------------------------------------------------------------
    # Formatting the input so that it's ready to be passed to mainFunc(*input)
    # ------------------------------------------------------------------------
    formattedInput = \
        [
            [
                int(num) for num in inputLines[caseStartIndex[caseID]].split(colSep)
            ]
            for caseID in range(T)
        ]
    # ------------------------------------------------------------------------
    # ------------------------------------------------------------------------------------------------------------

    # ------------------------------------------------------------------------------------------------------------
    # Generating the output : Apply mainFunc() to each test case
    # ------------------------------------------------------------------------------------------------------------
    outputString = "\n".join(["Case #"+str(i+1)+": "+main_func(*inp) for i, inp in enumerate(formattedInput)])
    print("output:")
    print(outputString)
    with open("output.txt", "w") as outputFile:
        outputFile.write(outputString)
    # ------------------------------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------------------------------------------------