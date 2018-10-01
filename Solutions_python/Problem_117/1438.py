def mowable(input):
    lines = input.split('\n')
    cases = int(lines[0])
    line_num = 1
    f1 = file("input_small_lawn.txt",'w+b')


    for i in range(cases):
        dimensions = lines[line_num].split(" ")
        line_num += 1
        height = int(dimensions[0])
        width = int(dimensions[1])
        lawn = []
        for j in range(height):
            lawn.append(lines[line_num].split(" "))
            line_num += 1
        if reachable(lawn,height,width):
            f1.write("Case #" + str(i+1) + ": YES" + "\n")
        else:
            f1.write("Case #" + str(i+1) + ": NO" + "\n")

def reachable(lawn,height,width):
    for i in range(height):
        for j in range(width):
            curr = int(lawn[i][j])
            row_escape = True
            col_escape = True
            for k in range(width):
                if int(lawn[i][k]) > curr:
                    row_escape =  False
            for l in range(height):
                if int(lawn[l][j]) > curr:
                    col_escape = False
            if row_escape or col_escape:
                pass
            else:
                return False

    return True
            

test = """3
3 3
2 1 2
1 1 1
2 1 2
5 5
2 2 2 2 2
2 1 1 1 2
2 1 2 1 2
2 1 1 1 2
2 2 2 2 2
1 3
1 2 1"""

input = """
