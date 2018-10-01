import sys

if __name__ == "__main__":
    inputfile = "A-small-attempt0.in"
    outputfile = "out.txt"
    f = open(inputfile)
    g = open(outputfile, "ab")
    t = int(f.readline().strip())

    for n in range(t):
        rowguess = int(f.readline().strip())
        cards = dict()
        for k in range(4):
            cards[k+1] = f.readline().split()
        candidate_cards = cards[rowguess]

        rowguess2 = int(f.readline().strip())


        newcards = dict()
        for k in range(4):
            newcards[k+1] = f.readline().split()
        candidate_cards2 = newcards[rowguess2]

        solutions = []
        for element in candidate_cards:
            if element in candidate_cards2:
                solutions.append(element)
        if len(solutions) == 0:
            result = "Volunteer cheated!"

        elif len(solutions) > 1:
            result = "Bad magician!"
        else: 
            result = solutions[0]

        m = n+1
        string_res = "Case #" + str(m) + ": " + result +'\n'
        sys.stdout.write(string_res)
        g.write(string_res.encode("ASCII"))

