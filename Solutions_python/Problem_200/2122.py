
def resolve_case():
    num = int(input())
    num_list = list(str(num))
    assend_index = 0
    same=1
    for assend_index in range(1, len(num_list)):
            if num_list[assend_index - 1] > num_list[assend_index]:
                break;
            elif num_list[assend_index - 1] == num_list[assend_index]:
                same += 1
            else:
                same = 1
    print("".join(num_list[:assend_index-same]), end="")

    num_list_tmp = num_list[assend_index-same:]
    num_list_sorted = num_list[assend_index-same:]
    num_list_sorted.sort()
    length = len(num_list_tmp)
    for x in range(0, length):
        if num_list_tmp[x] is num_list_sorted[x]:
            print(num_list_tmp[x], end="")
        else:
            print(int(str(int(num_list_tmp[x]) - 1) + ("9" * (length - x - 1))), end="")
            break
    return

cases = int(input())

for case in range(0, cases):
    print("Case #" + str(case + 1), end=": ")
    resolve_case()
    print()
