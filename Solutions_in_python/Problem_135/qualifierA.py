__author__ = 'RTSwan'


def get_lines(infile):
    """Returns a list containing the lines in a file, supplied as infile"""
    file = open(infile, "r")
    linesTemp, lines = [], []
    for i in file:
        linesTemp.append(i)
    file.close()
    for i in linesTemp:
        lines.append(i.replace("\n", ""))
    return lines


def gen_list(line1, line2, line3, line4):
    """Generates a list of integers from the 4 strings supplied"""
    cardlistStr = []
    cardlistInt = []
    cardlistStr.append(line1.split(" "))
    cardlistStr.append(line2.split(" "))
    cardlistStr.append(line3.split(" "))
    cardlistStr.append(line4.split(" "))
    for i in cardlistStr:
        temp = []
        for j in i:
            temp.append(eval(j))
        cardlistInt.append(temp)
    return cardlistInt


def check_overlap(list1, list2):
    """Checks if there are any integers in list1 that appear in list2"""
    found = False #check if a match has been found
    number = -1 #store the index of the match number
    duplicate = False #check if there are duplicate matches
    for i in list1:
        if list2.__contains__(i):
            if not found:
                number = i
                found = True
            elif not duplicate:
                duplicate = True
    if not found and not duplicate:
        return "Volunteer cheated!"
    elif found and not duplicate:
        return str(number)
    else:
        return "Bad magician!"

def magic_trick(infile, outfile):
    """Takes the input from infile to find the result of the magic trick.
    Answers are written to the file outfile (for Google CodeJam qualifier 2014)"""
    lines = get_lines(infile)
    outputfile = open(outfile, "w")
    cases = eval(lines[0])
    count = 1
    case = 1
    while count < len(lines):
        firstans = eval(lines[count])
        count += 1
        firstlist = gen_list(lines[count], lines[count + 1], lines[count + 2], lines[count + 3])
        count += 4
        secondans = eval(lines[count])
        count += 1
        secondlist = gen_list(lines[count], lines[count + 1], lines[count + 2], lines[count + 3])
        ans = check_overlap(firstlist[firstans - 1], secondlist[secondans - 1])
        print("Case #" + str(case) + ": " + ans, file=outputfile)
        case += 1
        count += 4
    outputfile.close()

if __name__ == "__main__":
    magic_trick("A-small-attempt.in", "a-small-output.txt")