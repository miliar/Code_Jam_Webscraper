fl_in = open('A-large.in', 'r')
fl_out = open('A-large.out', 'w')
inp_list = list()
case_num = 1

for num in fl_in:
    inp_list.append(num.split())

fl_in.close()

del inp_list[0]

for elem_count in inp_list:

    shy_lvl = 0
    member_need = 0
    stand_memb_count = 0

    for memb in elem_count[1]:
        imemb = int(memb)
        if shy_lvl == 0:
            if imemb == 0:
                member_need = 1
                stand_memb_count = 1
                shy_lvl += 1
                continue
            else:
                stand_memb_count = imemb
        else:
            if shy_lvl <= stand_memb_count:
                stand_memb_count += imemb
            else:
                if imemb == 0:
                    shy_lvl += 1
                    continue
                else:
                    member_need += shy_lvl - stand_memb_count
                    stand_memb_count += shy_lvl - stand_memb_count + imemb
        shy_lvl += 1
    fl_out.write('Case #' + str(case_num) + ': ' + str(member_need) + '\n')
    case_num += 1
fl_out.close()