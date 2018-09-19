import sys

filename = sys.argv[1]
def magician(filename):
    fh = open(filename)
    times = int(fh.readline().strip())

    time = 1
    while time <= times:
       blocks=[]
       count = 10
       while count > 0:
          nums = fh.readline().strip().split()
          blocks.append([int(x) for x in nums])
          count -= 1
       output(blocks, time)
       time += 1
    fh.close()

def output(blocks, time):
    lineNum1 = blocks[0][0]
    lineNum2 = blocks[5][0]
    list1 = blocks[lineNum1]
    list2 = blocks[lineNum2+5]
    guess = []
    for i in list1:
        if i in list2:
            guess.append(i)

    if len(guess) == 1:
        res = guess[0]
    elif len(guess) > 1:
        res = "Bad magician!"
    else:
        res = "Volunteer cheated!"
    print("Case #" + str(time) + ": " + str(res))

magician(filename)

