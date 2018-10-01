def number_flipping(S, K):
    """
    Given a string S of + and - and a size K of the pancake flipper, determine how many flips are necessary 
     to flip all the pancakes to the + side
    :param S: a string of + or -
    :param K: size of the humongous pancake flipper 
    :return: either an int containing the number of flipping or a string: IMPOSSIBLE 
    """
    L = len(S)
    parity = K % 2
    happy, blank = calculate_happy_faces(S)
    if blank == 0:
        return 0
    if blank % 2 == 1 and parity == 0:
        return "IMPOSSIBLE"
    count = 0
    for i in range(len(S)):
        if S[i] == "-" and i + K <= len(S):
            S = flip(S, i, K)
            count += 1
    if all(c == "+" for c in S):
        return count
    else:
        return "IMPOSSIBLE"


def flip(S, start, K):
    """
    Flip the values between S[i] and S[i+K-1]   
    :param S: a string of + and -
    :param start: the left-most index at which to flip
    :param K: size of the humongous pancake flipper
    :return: 
    """

    R = ""
    for i in range(len(S)):
        if start <= i < start + K:
            R += "+" if S[i] == "-" else "-"
        else:
            R += S[i]
    return "".join(R)


def calculate_happy_faces(S):
    """
    Given a string of + (happy faces) and - (blank faces), calculate how many happy and blank faces are there 

    :param S: a string of + or -
    :return: two integers, number of happy and of blank faces 
    """

    happy = sum(c == "+" for c in S)
    blank = len(S) - happy
    return happy, blank


with open("./A-large.in", "r") as fin:
    with open("./A-large.out", "w+") as fout:
        T = int(fin.readline().strip("\n"))

        for i in range(T):
            S, K = fin.readline().strip("\n").split()
            K = int(K)
            res = number_flipping(S, K)
            if isinstance(res, int):
                fout.write("Case #%d: %d\n" % (i + 1, res))
            else:
                fout.write("Case #%d: IMPOSSIBLE\n" % (i + 1))
