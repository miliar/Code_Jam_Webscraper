S = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
G = ['y','n','f','i','c','w','l','b','k','u','o','m','x','s','e','v','z','p','d','r','j','g','t','h','a','q']
num = ['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30']
dic = {}
for (s,g) in zip(S,G):
    dic[g] = s

fin = open('A-small-attempt0.in','r')
fout = open('output.out','w')
T = eval(fin.readline())
for i in range(T):
    g = fin.readline()
    fout.write("Case #")
    fout.write(num[i+1])
    fout.write(": ")
    tmp = ''
    for ch in g:
        if (ch >= 'a' and ch <= 'z'):
            tmp = tmp + dic[ch]
        else:
            tmp = tmp + ch
    fout.write(tmp)
fin.close()
fout.close()
