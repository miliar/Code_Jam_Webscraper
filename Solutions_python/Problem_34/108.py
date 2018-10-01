#!/usr/bin/env python

def main():
    dict = [];
    fin = open("A-large.in","r");
    fout = open("output.out","w");
    st = [];
    st = (fin.readline().split());
    L = int(st[0]);
#    print L;
    D = int(st[1]);
    N = int(st[2]);
    for i in range(D):
        dict.append(fin.readline());
    flag = 0;
    for i in range(N):
        str = fin.readline()[:-1];
        word = [];
#        print str.__len__();
        for j in range(str.__len__()):
            if str[j] == '(':
                flag = 1;
                word.append(set());
            elif str[j] == ')':
                flag = 0;
            else:
                if flag == 0:
                    word.append(set(str[j]));
                else:
                    word[word.__len__()-1].add(str[j]);
#        print word.__len__();

        if word.__len__() != L:
            fout.write("Case #{0}:  0\n".format(i+1));
            continue;

        ans = 0;
        for d in range(D):
            success = 1;
            for j in range(L):
                if dict[d][j] not in word[j]:
                    success = 0;
                    break;
            if success == 1:
                ans += 1;
        fout.write("Case #{0}:  {1}\n".format(i+1, ans));
    

if __name__ == '__main__':
    main();
