
# def process(lst, num):
#     n = num
#     for e in lst:
        
#         if e <= n:
#             pass
#         else: # e > n
#             e -= (num - n)
#             print "e:" + str(e)
#             while e > n:
#                 n -= 1
#                 e -= n
#                 print "e:" + str(e)
#                 print "n:" + str(n)
#                 if n == 0:
#                     return False
#     return True

def process(lst, num):
    n = num
    for i in range(n):
        lst2 = lst[:]
        
        # print i
        # print lst2
        for j in range(i):
            # cut and put to lst2
            elem = lst2[-1]
            h1 = num - i
            h2 = elem - h1
            # print h2
            for ii in range(len(lst2)):
                if lst2[ii] > h2:
                    lst2.insert(ii, h2);
                    break
            # if len(lst) == len(lst2):
            #     lst2.insert(ii, h2);
            lst2 = lst2[:-1]
            # print lst2
        tr = True
        for elem in lst2:
            if elem > num - i:
                tr = False
        if tr:
            return True

    return False

# def process(lst, num):
#     n = num
#     i = 1
#     for e in lst:
        
#         if e <= n:
#             pass
#         else: # e > n
#             e -= (num - n)
#             # print "e:" + str(e)
#             while e > n:
#                 n -= 1
#                 e -= n
#                 # print "e:" + str(e)
#                 # print "n:" + str(n)
#                 # print lst
#                 #swap
#                 if (len(lst) > i) and lst[i] - (num - n) > e:
#                     temp = e + (num - n)
#                     e = lst[i] - (num - n)
#                     lst[i] = temp

#                 if n == 0:
#                     return False
#         i += 1
#     return True


# def process(lst, num):
#     n = num
#     # for e in lst:
#     while lst != []:
#         e = lst[-1]

#         if e <= n:
#             pass
#         else: # e > n
#             e -= (num - n)
#             # print "e:" + str(e)
#             # while e > n:
#             n -= 1
#             e -= n

#             if n == 0:
#                 return False

#             for i in range(len(lst)):
#                 if lst[i] > e:
#                     lst.insert(i, e);
#                     break;
#             lst = lst[:-1]
#             # print "e:" + str(e)
#             # print "n:" + str(n)
            
#     return True


def all_perms(elements):
    if len(elements) <=1:
        yield elements
    else:
        for perm in all_perms(elements[1:]):
            for i in range(len(elements)):
                # nb elements[0:1] works in both string and list contexts
                yield perm[:i] + elements[0:1] + perm[i:]

def main():
    filename = "input.txt"
    filename = "B-small-attempt9.in"
    inpfile = open(filename, 'r')
    outfile = open('outfile', 'w')
    casenum = int(inpfile.readline().strip())
    for case in range(1, casenum + 1):
        line = inpfile.readline().strip()
        line1 = inpfile.readline().strip()
        linelst = line1.split()
        
        D = int(line)
        P = linelst
        lst = []
        for e in linelst:
            lst.append(int(e))
        lst.sort(reverse=False)
        print lst

        ret = 1008

        # for el in all_perms(lst):

        att = 1
        while 1:
            if process(lst[:], att):
                break
            att += 1
        ret = min(att, ret)

        # print D
        # print P

        result = "Case #" + str(case) + ": " + str(att) + "\n"
        print result
        outfile.write(result)
    inpfile.close()
    outfile.close()




if __name__ == "__main__":


    main()

    # l = [1,2,3]
    # for e in all_perms(l):
    #     print e

    