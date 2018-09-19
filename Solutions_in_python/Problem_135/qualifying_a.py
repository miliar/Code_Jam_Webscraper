#! /usr/bin python



def output(case, answer, card=0):
    if answer == 0:
        return "Case #{}: {}\n".format(case, "Volunteer cheated!")
    elif answer > 1:
        return "Case #{}: {}\n".format(case, "Bad magician!")
    else:
        return "Case #{}: {}\n".format(case, card)

def main():
    with open("A-small-attempt1.in", "r") as inputfile:
        inputfile = inputfile.readlines()
        #print inputfile

        numberofcases = int(inputfile[0])
        case = 1

        while case <= numberofcases:
            firstanswer = int(inputfile[1+10*(case-1)])-1

            cards = inputfile[2+10*(case-1) + firstanswer].strip().split(" ")

            secondanswer = int(inputfile[6+10*(case-1)])-1

            morecards = inputfile[7+10*(case-1) + secondanswer].strip().split(" ")

            print cards
            print morecards

            cardcount = 0
            for card in cards:
                if card in morecards:
                    cardcount += 1

            if cardcount == 1:
                finalcard = set(cards) & set(morecards)
                finalcard = finalcard.pop()
            else:
                finalcard = 0
            
            print cardcount, finalcard
            with open("output.txt", "a") as outfile:
                outfile.write(output(case, cardcount, finalcard))

            #raw_input()

            case += 1


if __name__ == '__main__':
    main()
