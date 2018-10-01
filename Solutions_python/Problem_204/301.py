import math

def main():
    t = int(input())
    cases = []
    for i in range(0, t):
        line = input()
        nums = line.split()
        n = int(nums[0])
        p = int(nums[1])
        line = input()
        ing_amounts = list(map(float, line.split()))
        q = []
        for j in range(0, n):
            line = input()
            qi = list(map(float, line.split()))
            q.append(qi)
        cases.append((n,p,ing_amounts,q))
    case_num = 1

    for case in cases:
        (n,p,amounts,q) = case
        servs = []
        used_pack = []
        for i in range(0, n):  # for each ingredient.
            servs.append([])
            used_pack.append([])
            for j in range(0, p):  # for each package.
                min_serv = math.ceil(q[i][j]/(float(amounts[i])*1.1))
                max_serv = math.floor(q[i][j]/(float(amounts[i])*0.9))
                if min_serv > max_serv:
                    min_serv, max_serv = 0, 0
                servs[i].append((min_serv,max_serv))

        # Determine number of kits that can be made.
        kits = count_kits(servs, used_pack)
        print('Case #{0}: {1}'.format(case_num, kits))
        case_num += 1


def count_kits(servs, used_pack):
    #print(used_pack)
    max_kit = 0
    if len(servs) == 1:  # count number of packages != 0 servs
        kit_sum = 0
        for pack in servs[0]:
            if pack[1] > 0:
                kit_sum += 1
        max_kit = kit_sum
    elif len(servs) == 2:
        #print(servs)
        if len(servs[0]) == 0: return 0
        kit_sum = 0
        for j in range(0, len(servs[1])):
            #if j in used_pack[1]: continue
            new_used1 = used_pack[0] + [0]
            new_used2 = used_pack[1] + [j]
            new_used = [new_used1, new_used2]
            new_servs1 = servs[0][1:]
            new_servs2 = servs[1][:j] + servs[1][j+1:]
            new_servs = [new_servs1, new_servs2]
            kit_sum = is_kit([servs[0][0], servs[1][j]]) + count_kits(new_servs, new_used)
            if kit_sum > max_kit: max_kit = kit_sum
    return max_kit

'''
def pick_pack_indices(servs):

'''
def is_kit(packs):
    if len(packs) == 0: return
    min_serv = packs[0][0]
    max_serv = packs[0][1]
    for pack in packs:
        if max_serv == 0: return False
        if pack[1] < min_serv or pack[0] > max_serv:
            return False
        min_serv = max(min_serv, pack[0])
        max_serv = min(max_serv, pack[1])
    if max_serv == 0: return False
    return True

main()
