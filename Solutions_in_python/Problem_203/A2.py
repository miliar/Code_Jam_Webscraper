import sys
testnum = int(input().strip())

for k in range(testnum):
    R, C = map(int, input().strip().split(" "))
    lines = []
    string_set = []
    first_line_flag = 0
    for _ in range(R):
        string_set.append(input().strip())

    for i in range(R):
        nonq_p = []
        nonq_l = []
        string = string_set[i]
        line = ''

        if i == 0 and string == '?'*C:
            lines.append('0')
            first_line_flag += 1
        elif i == first_line_flag and string == '?'*C:
            lines.append('0')
            first_line_flag += 1
        else:
            for j in range(C):
                if string[j] != '?':
                    nonq_p.append(j)
                    nonq_l.append(string[j])
            len_non = len(nonq_p)
            if len_non == 1:
                line += nonq_l[0]*C
            elif len_non == 0:
                line += lines[i-1]
            else:
                for l in range(len_non):
                    if l == 0:
                        line += nonq_l[0] * nonq_p[1]
                    elif l == len_non-1:
                        line += nonq_l[l] * (C-nonq_p[l])
                    else:
                        line += nonq_l[l] * (nonq_p[l+1]-nonq_p[l])
            lines.append(line)
    
    print("Case #"+str(k+1)+":")
    if first_line_flag == 0:
        print('\n'.join(lines))
    else:
        for a in range(first_line_flag):
            lines[a] = lines[first_line_flag]
        print('\n'.join(lines))

