
inp = open("in.txt", 'r')
out = open("out.txt", 'w')
num_case = 0

for line in inp:
    if num_case is 0:
        num_case += 1
        continue
    line_list = line.split()
    list_last_num = list(line_list[0])
    last_num = [int(c) for c in list_last_num]
    for i in range(1, len(last_num)):
        if int(last_num[i-1]) > int(last_num[i]):
            for j in range(i, len(last_num)):
                last_num[j] = 9
            for j in range(i):
                k = i-j-1
                if last_num[k] > 0:
                    last_num[k] -= 1
                    if k != 0 and last_num[k] < last_num[k-1]:
                        last_num[k] = 9
                        continue
                    break
    tidy_list = [str(m) for m in last_num]
    s = ""
    out.write("Case #" + str(num_case) + ": "+str(int(s.join(tidy_list)))+"\n")
    num_case += 1

out.close()
inp.close()