# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
def isPossibleToFlip(row,f_size):
    out = []
    flip_count = 0
    dic = {}

    for i in range(0,len(row) - flipper_size + 1):
        if(row[i] == '-'):
            row = flipIt(i,f_size,row)
            flip_count += 1
    #print("+++++  " + row)
    if isAllDone(row):
        out.append(flip_count)
        return flip_count
    return 0

#         change -+* only if it is -++

def flipIt(from_i,len_fp,inp_str):

    if from_i > len(inp_str) - len_fp:
        return inp_str
    temp = ""

    for i in inp_str[from_i:from_i+len_fp]:
        if i == '+':
            temp += '-'
        else:
            temp += '+'
    if from_i == 0:
        return temp + inp_str[from_i+len_fp : len(inp_str)]
    else:
        if from_i+len_fp < len(inp_str):
            return inp_str[0 : from_i ] + temp + inp_str[from_i+len_fp : len(inp_str)]
        else:
            return inp_str[0: from_i] + temp

    return

def isAllDone(inp_str):
    return inp_str.startswith('+'* len(inp_str))


t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    inp = input().split(" ")
    cake_row = inp[0]
    flipper_size = int(inp[1])
    count = 0
    if len(cake_row) < flipper_size:
        if isAllDone(cake_row):
            count = 0
        else:
            count = "IMPOSSIBLE"
        print("Case #{}: {}".format(i, count))

        # dic["possible"] = isAllDone(row)
        # dic["count"] = 0
        # out.append(flip_count)
    #reduce problem to flipper size, if after flipping we can arrange same side to flipped ones or to their neighbours do that
    #  ---+-++-
    # ++----+-+
    # flppig pattern -++- --- --+-- -+-+
    # ---
    # -++-
    # -++
    # +----++-


    if not isAllDone(cake_row):
        count = isPossibleToFlip(cake_row,flipper_size)
        if count == 0:
            count = "IMPOSSIBLE"
    else:
        count = 0
    print("Case #{}: {}".format(i, count))


  # n, m = [int(s) for s in input().split(" ")]  # read a list of integers, 2 in this case
  #
  # check out .format's specification for more formatting options



