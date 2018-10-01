import random
fname = 'D-large.in'
with open(fname) as f:
    Data = f.read().splitlines()
data = []
for i in Data:
    data.append([float(j) for j in i.split()]) if len(i.split()) > 1 else data.append(float(i))
NumCases = data[0]
del data[0]
Cases = []
n,m = 3,0
for i in xrange(int(NumCases)):
    Cases.append(data[m:n])
    n += 3
    m += 3
C = 1
while Cases:
    Case = Cases.pop(0)
    Naomi = Case[1][:] if type(Case[1]) == list else [Case[1]][:]
    Ken = Case[2][:] if type(Case[2]) == list else [Case[2]][:]
    Deceitful,War = 0,0
    #Deceitful
    while Naomi:
        if max(Naomi) < max(Ken):
            del Naomi[Naomi.index(min(Naomi))]
            del Ken[Ken.index(max(Ken))]
        elif max(Naomi) > max(Ken):
            del Naomi[Naomi.index(max(Naomi))]
            del Ken[Ken.index(max(Ken))]
            Deceitful += 1
    #War
    Naomi = Case[1][:] if type(Case[1]) == list else [Case[1]][:]
    Ken = Case[2][:] if type(Case[2]) == list else [Case[2]][:]
    while Ken:
        ChoiceNaomi = random.choice(Naomi)
        del Naomi[Naomi.index(ChoiceNaomi)]
        try:
            ChoiceKen = min([i for i in Ken if i > ChoiceNaomi])
            del Ken[Ken.index(ChoiceKen)]
        except ValueError:
            del Ken[Ken.index(min(Ken))]
            War += 1
    print "Case #" + str(C) + ": " + str(Deceitful) + " " + str(War)
    C += 1