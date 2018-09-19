def main():
    fp =open("A-large.in")
    fout = open("output.out","w")
    t = int(fp.readline())
    for j in range(0,t):
        str1 = fp.readline()
        arr= str1.split()
        n = int(arr[0])

        frnds=0
        ppl_clapping=0
        string = arr[1]
        for i in range (0,n):
            ppl_clapping = ppl_clapping+int(string[i])

            if ppl_clapping <= i:
                frnds = frnds+1
                ppl_clapping = ppl_clapping + 1
            
        sj = str(j+1)
        scnt =str(frnds)
        outstr = str("Case #"+sj+": "+scnt+"\n")
        fout.write(outstr)
        #fout.write(str(outstr))

    fp.close()
    fout.close()
    
main()

        
