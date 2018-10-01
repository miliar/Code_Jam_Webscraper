#!/usr/bin/python2.7

fichier = open("test","r")
fresult = open("result","w")

print ("COMPUTATION LAUNCHED")
T=0
i=1

for line in fichier:
    if T==0:
        T=int(line.strip('\n'))
    else:
        #CODE HERE
        res=0
        S=int(line.strip('\n'))
        print S
        if S<10:
            res=S
        else:
            S=str(S)
            while res==0:
                taunt=0
                if res!=0:
                    break
                elif int(S)<10:
                    res=int(S)
                else:
                    for n in range(0,len(S)-1):
                        if int(S[n])>int(S[n+1]):
                            if taunt==0:
                                SS=str(int(S)-1)
                                print SS
                                taunt=1
                    if taunt==0:
                        res=int(S)
                    else:
                        S=SS
            print res
        res=str(res)
                    
        #END CUSTOM CODE
        fresult.write("Case #"+str(i)+": "+res+"\n")
        i+=1

fichier.close()
fresult.close()
