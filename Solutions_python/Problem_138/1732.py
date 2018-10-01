#! /usr/bin python

def main():
    resultado = []

    score = { 'decieve': 0, 'nondecieve': 0}

    with open("input.txt", "r") as inputfile:
        inputfile = inputfile.readlines()

        ##print inputfile

        numberofcases = int(inputfile[0])

        case = 1

        while case <= numberofcases:
            blocks = map(int, inputfile[1+3*(case-1)].strip().split())
            
            naomi = map(float, inputfile[2+3*(case-1)].strip().split())
            ken = map(float, inputfile[3+3*(case-1)].strip().split())

            blocks1 = blocks[:]
            naomi1 = naomi[:]
            ken1 = ken[:]
            #print case
            #print blocks, blocks1
            #print naomi
            #print ken
            score['decieve']=0
            score['nondecieve']=0
            i = 1
            while i <= 2:
                #print "i ", i
                if i == 1:
                    while blocks[0] > 0:
                        ken_max = max(ken)
                        naomi_max = max(naomi)

                        if naomi_max < ken_max:
                            naomi_min = min(naomi)
                            naomi.remove(naomi_min)
                            ken.remove(ken_max)

                        else:
                            score['decieve'] += 1
                            naomi.remove(naomi_max)
                            ken.remove(ken_max)

                        

                        blocks[0] -= 1
                    #print "Decieve ",
                    #print score['decieve']
                if i == 2:
                    ##print "here!"
                    ##print blocks1[0]
                    while blocks1[0] > 0:
                        ken_max = max(ken1)
                        naomi_max = max(naomi1)

                        ##print naomi_max
                        ##print ken_max
                        ##print "yooo"
                        if naomi_max > ken_max:
                            ken_min = min(ken1)
                            score['nondecieve'] += 1
                            naomi1.remove(naomi_max)
                            ken1.remove(ken_min)

                        else:
                            naomi1.remove(naomi_max)
                            ken1.remove(ken_max)

                        

                        blocks1[0] -= 1
                    #print "nondecieve ",
                    #print score['nondecieve']

                i += 1


            
            
            resultado.append("Case #{}: {} {}".format(case,score['decieve'],score['nondecieve']))
            case += 1

    
    with open("outputd.txt", "w") as outfile:
        outfile.write("\n".join(resultado))

if __name__ == '__main__':
    main()