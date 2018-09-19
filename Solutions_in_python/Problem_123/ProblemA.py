'''
Created on Apr 29, 2013

@author: mac
'''
import io, sys
# f = open("../input/test1")
# o = open("../output/test1", 'w')

f = open("../input/A-small-practice.in")
o = open("../output/A-small-practice.out", 'w')

lines = f.readlines()
cases = int(lines[0])
print cases 
#for c in range(1,2):
for c in range(1, cases + 1):
    A = int(lines[2 * (c - 1) + 1].split()[0])
    N = int(lines[2 * (c - 1) + 1].split()[1])
    Bi = [int(i) for i in lines[2 * c].split()]
    
    Bi.sort()
    amount_change = 0
    rip_alls_from_i = False
    i = 0
    while i < len(Bi):
        amount_consume_self_temp = 0
        while A <= Bi[i]:
            A += A - 1
            amount_consume_self_temp += 1
            if amount_consume_self_temp == len(Bi) - i:
                rip_alls_from_i = True
                amount_change  += len(Bi) - i
                break
        if rip_alls_from_i:
            break 
        amount_change += amount_consume_self_temp        
        A += Bi[i]
        i += 1
    print 'Case %d : A = %d, B = %d, Bi = %s' % (c, A, N , Bi)
    print('Case #%d: %d\n' % (c,amount_change))
    o.write('Case #%d: %d\n' % (c,amount_change))
#     else:
#         for i in range(len(Bi)):
#             if At <= Bi[i]:
#             mount_not_solve += 1
#          else:
#              At += Bi[i]
#          print 'Case %d : A = %d, B = %d, Bi = %s' % (c, A, N , Bi)
#     need = False
#     for i in range(len(Bi)):
#         if At <= Bi[i]:
#             need = True
#             amount_not_solve += 1
#         else:
#             At += Bi[i]
#     print 'Case %d : A = %d, B = %d, Bi = %s' % (c, A, N , Bi)
#     print(' #################################### ')
#     if not need:
#         print('Case #%d: %d\n' % (c,0))
#         o.write('Case #%d: %d\n' % (c,0))
#     else:
#         amount_consume_self = 0
#         solve_mix = 0
#         consume_valid = True
#         At = A
#         for i in range(len(Bi)):
#             amount_consume_self_temp = 0
#             while At <= Bi[i]:
#                 At += At - 1
#                 amount_consume_self_temp += 1
#                 if At == A:
#                     consume_valid = False
#                     break
#                 if amount_consume_self_temp == len(Bi) - i - 1:
#                     solve_mix  = amount_consume_self + len(Bi) - i - 1
#             amount_consume_self += amount_consume_self_temp
#             if not consume_valid:
#                 break
#             At += Bi[i]
#         
#         if not consume_valid:
#             amount_consume_self = amount_not_solve + 1
#     
#         amount_change = min(amount_consume_self, amount_not_solve)
# #         if solve_mix == 0:
# #             amount_change = min(amount_consume_self, amount_not_solve)
# #         else:
# #             amount_change = solve_mix
#         print('Case #%d: %d\n' % (c,amount_change))
#         o.write('Case #%d: %d\n' % (c,amount_change))
        
        
#    print 'Case %d : A = %d, B = %d, Bi = %s' % (c, A, N , Bi)
f.close()
