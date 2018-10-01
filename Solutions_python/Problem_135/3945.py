def process(row1,deck1,row2,deck2):
    possibles1 = deck1[row1-1]
    possibles2 = deck2[row2-1]
    rem = possibles1.intersection(possibles2)
    if len(rem) == 1:
        return str(rem.pop())
    if len(rem) == 0:
        return "Volunteer cheated!"
    else:
        return "Bad magician!"

def main():
    for cases in xrange(int(raw_input())):
        row1 = int(raw_input())
        deck1 = [set(int(x) for x in raw_input().split()) for i in xrange(4)]
        row2 = int(raw_input())
        deck2 = [set(int(x) for x in raw_input().split()) for i in xrange(4)]
        print "Case #%d: %s" % (cases + 1, process(row1,deck1,row2,deck2))
        
if __name__ == "__main__":
    main()