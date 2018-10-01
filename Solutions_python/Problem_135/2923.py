
def grabrows():
    rownum = int(raw_input())
    for j in xrange(4):
        if j == rownum - 1:
            row = set(map(int, raw_input().split(" ")))
        else:
            raw_input()
    return row

def main():
    cases = int(raw_input())
    for case in xrange(cases):
        rowone = grabrows()
        rowtwo = grabrows()
        answers = rowone & rowtwo
        if len(answers) == 1:
            print ("Case #" + str(case + 1) + ": " + str(answers.pop()))
        elif len(answers) == 0:
            print ("Case #" + str(case + 1) + ": Volunteer cheated!")
        else:
            print ("Case #" + str(case + 1) + ": Bad magician!")
        
       
        
if __name__ == "__main__":
    main()
