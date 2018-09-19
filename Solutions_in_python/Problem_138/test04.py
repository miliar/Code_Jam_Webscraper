i = 0
t = 0
with open('test04.out', 'w') as out_file:
    for line in open('D-large.in'):
            i = i + 1
            if i == 2:
                n = int(line)
            elif i == 3:
                inputs = line.split()
                Naomi = []
                for word in inputs:
                    Naomi.append(float(word))
                
            elif i == 4:
                inputs = line.split()
                Ken = []
                for word in inputs:
                    Ken.append(float(word))
                Naomi.sort()
                Ken.sort()
                a = len(Ken)
                Ken_War = list(Ken)
                for j in Naomi:
                    for k in range(a):
                        if (Ken_War[k] > j):
                            Ken_War.remove(Ken_War[k])
                            break
                    if (a == len(Ken_War)):
                        break
                    else:
                        a = len(Ken_War)
                War_Result = a
                
                b = len(Naomi)
                Naomi_temp = list(Naomi)
                for j in Naomi_temp:
                    if (Ken[0] > j):
                        Naomi.remove(j)
                        Ken.remove(Ken[-1])
                    if (b == len(Naomi)):
                        break
                    else:
                        b = len(Naomi) 
                c = 0
                Naomi_temp = list(Naomi)
                for j in Naomi_temp:
                    if (Ken[0] < j):
                        c = c + 1
                        Naomi.remove(j)
                        Ken.remove(Ken[0])
                    else:
                        Naomi.remove(j)
                        Ken.remove(Ken[-1])
                Dec_War_Result = c    
                
                t = t + 1
                i = 1
                statement = "Case #" + str(t) + ": " + str(Dec_War_Result) + " " + str(War_Result)
                out_file.write("%s\n" % statement) 
            elif i == 1:
                m = int(line)