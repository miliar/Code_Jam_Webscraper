__author__ = 'fcueto'

from fractions import Fraction

#file_in = 'B-large.in'
file_in = 'D-large.in'
fid_in = open(file_in, 'r')
fid_out = open('war_large_out.txt','w')

N_cases = int(fid_in.readline().strip())

# def deceit(naomi, ken) :
#
#     if len(naomi)==1:
#         if naomi[0]>ken[0]:
#             return 1
#     else:
#         if naomi[0] < ken[0]:
#             return deceit(naomi[1:], ken[1:])
#         else
#             fo

for case in range(0, N_cases) :

    N_blocks = int(fid_in.readline().strip())

    naomi_lst = fid_in.readline().strip().split()
    ken_lst = fid_in.readline().strip().split()

    naomi = [Fraction(x) for x in naomi_lst]
    ken = [Fraction(x) for x in ken_lst]

    naomi.sort()
    ken.sort()


    # play War
    war = 0;
    while len(naomi) > 0 :

        naomi_block = naomi.pop()

        naomi_won = True
        for j in range(0, len(ken)):
            if ken[j]>naomi_block:
                ken.pop(j)
                naomi_won = False
                break
        if naomi_won:
            war = war + 1


    # play Deceitful War

    naomi = [float(x) for x in naomi_lst]
    ken = [float(x) for x in ken_lst]

    naomi.sort()
    ken.sort()

    dwar = 0;

    while len(naomi) > 0 :

        #print(naomi)
        #print(ken)
        #print('------')

        if naomi[0] > ken[0]:
            naomi.pop(0)
            ken.pop(0)
            dwar = dwar + 1
        else:
            naomi.pop(0)
            ken.pop(-1)


    line = "Case #%i: %i %i\n" % (case+1, dwar, war)
    print(line.strip())
    fid_out.write(line)

fid_in.close()
fid_out.close()