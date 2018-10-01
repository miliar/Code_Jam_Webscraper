out_text = "Case #%d: %d\n"

inp = open("in.txt", 'r')
out = open("out.txt", 'w')
num_case = 0

for line in inp:
    num_flips = 0
    if num_case is 0:
        num_case += 1
        continue
    line_list = line.split()
    pancake_string = list(line_list[0])
    k = int(line_list[1])
    for i in range(len(pancake_string)-k+1):
        if pancake_string[i] == '-':
            for j in range(k):
                if pancake_string[i+j] == '-':
                    pancake_string[i + j] = '+'
                else:
                    pancake_string[i + j] = '-'
            num_flips += 1
    is_impossible = False
    for i in range(len(pancake_string) - k +1, len(pancake_string)):
        if pancake_string[i] == '-':
            out.write( "Case #" + str(num_case) + ": IMPOSSIBLE\n")
            num_case += 1
            is_impossible = True
            break
    if not is_impossible:
        out.write("Case #" + str(num_case) + ": "+str(num_flips)+"\n")
        num_case += 1

out.close()
inp.close()