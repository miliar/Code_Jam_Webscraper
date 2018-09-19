arquivo = open('E:\\Documents and Settings\\ikke\\Desktop\\codejam\\C-small.in','r')
saida = open('C-small.out','w')


#not_a_real_code_jam_string = 'elcomew elcome to code jam'


quantidade = int(arquivo.readline())

for super_i in range(quantidade):
    not_a_real_code_jam_string = arquivo.readline()
    we_got_code_jam_dude = 0
    dic = {}

    for omg in range(len(not_a_real_code_jam_string)):
        try:
            dic[not_a_real_code_jam_string[omg]].append(omg)
        except:
            dic[not_a_real_code_jam_string[omg]] = [omg]

    if 'w' in dic and 'e' in dic and 'l' in dic and 'c' in dic and 'o' in dic and 'm' in dic and 'e' in dic and ' ' in dic and 't' in dic and 'o' in dic and 'c' in dic and 'o' in dic and 'd' in dic and 'j' in dic and 'a' in dic and 'm' in dic:
        for w in dic['w']:
            for e in dic['e']:
                if w > e:
                    continue
                for l in dic['l']:
                    if e > l:
                        continue
                    for c in dic['c']:
                        if l > c:
                            continue
                        for o in dic['o']:
                            if c > o:
                                continue
                            for m in dic['m']:
                                if o > m:
                                    continue
                                for e2 in dic['e']:
                                    if m > e2:
                                        continue
                                    for ws in dic[' ']:
                                        if e2 > ws:
                                            continue
                                        for t2 in dic['t']:
                                            if ws > t2:
                                                continue
                                            for o2 in dic['o']:
                                                if t2 > o2:
                                                    continue
                                                for ws2 in dic[' ']:
                                                    if o2 > ws2:
                                                        continue
                                                    for c3 in dic['c']:
                                                        if ws2 > c3:
                                                            continue
                                                        for o3 in dic['o']:
                                                            if c3 > o3:
                                                                continue
                                                            for d3 in dic['d']:
                                                                if o3 > d3:
                                                                    continue
                                                                for e3 in dic['e']:
                                                                    if d3 > e3:
                                                                        continue
                                                                    for ws3 in dic[' ']:
                                                                        if e3 > ws3:
                                                                            continue
                                                                        for j4 in dic['j']:
                                                                            if ws3 > j4:
                                                                                continue
                                                                            for a4 in dic['a']:
                                                                                if j4 > a4:
                                                                                    continue
                                                                                for m4 in dic['m']:
                                                                                    if w < e < l < c < o < m < e2 < ws < t2 < o2 < ws2 < c3 < o3 < d3 < e3 < ws3 < j4 < a4 < m4:
                                                                                        we_got_code_jam_dude +=1

        if we_got_code_jam_dude > 9999:
            we_got_code_jam_dude = str(we_got_code_jam_dude)[-4:]
        else:
            we_got_code_jam_dude = ('%04.0f' % we_got_code_jam_dude)[-4:]


        saida.write('Case #%i: %s\n' % (super_i+1, we_got_code_jam_dude))

    else:
        saida.write('Case #%i: 0000\n' % (super_i+1))

arquivo.close()
saida.close()
