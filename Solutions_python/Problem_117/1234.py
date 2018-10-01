# Lawnmower
# http://code.google.com/codejam/contest/2270488/dashboard#s=p1

def testHorizontal(tab,i,j,largeur):
    for k in range(largeur):
        if tab[i][k] > tab[i][j]:
            return False
    return True

def testVertical(tab,i,j,hauteur):
    for k in range(hauteur):
        if tab[k][j] > tab[i][j]:
            return False
    return True

def testPattern(tab,largeur,hauteur):
    for i in range(hauteur):
        for j in range(largeur):
            if not testHorizontal(tab,i,j,largeur) and \
               not testVertical(tab,i,j,hauteur):
                return 'NO'
    return 'YES'

f = open('B-large.in','r')

n = int(f.readline())

output = open('B-large.out','w')

for i in range(n):
    hauteur,largeur = map(int,f.readline().split())
    tab = []
    for j in range(hauteur):
        tab.append(map(int,f.readline().split()))
        #print(tab)
    output.write('Case #{}: {}\n'.format(i+1,testPattern(tab,largeur,hauteur)))
    #garb = f.readline()

output.close()
f.close()
