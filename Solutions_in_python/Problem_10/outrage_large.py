def calc(P,K,L,freq):
    freq_num = []
    for e in freq:
        freq_num.append(long(e))
    freq_num.sort()
    freq_num.reverse()
    press = long('0')
    i = 1
    mnoz = 1
    for el in freq_num:
       press = press + long(el)*mnoz
       if i%K == 0:
           mnoz = mnoz +1
       i = i+1
    return press
def outrage():
    f = open("A-large.in","r")
    fout = open("A-large.out","w")
    P = 0
    K = 0
    L = 0
    freq = []
    data_in = 1
    freq_in = 2
    knauter = 1
    try:
        i = 0
        for line in f:
            if i==0:
                #omit last \n
                #no_cases = int(line[0:len(line)-1])
                a = 1
            elif i==data_in:
                data = line.split(" ")
                P = int(data[0])
                K = int(data[1])
                L_tmp = data[2]
                L = int(L_tmp[0:len(L_tmp)-1])
                data_in = data_in+2
                if P*K < L:
                    fout.write("Case #"+str(knauter)+": Impossible\n")
                    knauter = knauter +1
            elif i==freq_in:
                freq = line.split(" ")
                freq[L-1]=freq[L-1][0:len(freq[L-1])-1]
                freq_in = freq_in+2
                press = calc(P,K,L,freq)
                fout.write("Case #"+str(knauter)+": "+str(press)+"\n")
                knauter = knauter +1
                freq = []
            i=i+1
    finally:
        f.close()
        fout.flush()
        fout.close()
if __name__ == "__main__":
    outrage()

