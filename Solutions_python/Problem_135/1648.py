__author__ = 'Lucas'


def testCase(answer1, answer2, array1, array2, w, num):
    possibleArray1 = array1[answer1-1]
    possibleArray2 = array2[answer2-1]
    intersects = False
    uniqueIntersect = True
    intersectValue = 0
    for card in possibleArray1:
        if card in possibleArray2:
            if intersects:
                uniqueIntersect = False
            else:
                intersects = True
                intersectValue = card
    if intersects and uniqueIntersect:
        w.write("Case #" + str(num) + ": " + str(intersectValue))
    elif intersects and not uniqueIntersect:
        w.write("Case #" + str(num) + ": " + "Bad magician!")
    else:
        w.write("Case #" + str(num) + ": " + "Volunteer cheated!")
    w.write("\n")

def main():
    f = open('input.in', 'r')
    w = open('output.out', 'w')

    T = int(f.readline().split()[0])
    for t in range(T):
        answer1 = int(f.readline().split()[0])
        array1 = []
        for i in range(4):
            array1.append(list(map(int, f.readline().split())))
        answer2 = int(f.readline().split()[0])
        array2 = []
        for i in range(4):
            array2.append(list(map(int, f.readline().split())))
        testCase(answer1, answer2, array1, array2, w, t+1)



if __name__ == "__main__": main()