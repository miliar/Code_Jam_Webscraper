#!/usr/bin/python2.7

import random

# def select_optimal2(input, blocks):
#
#     lowest = None
#
#     for v in blocks:
#         if (input < v):
#             if lowest == None or v < lowest:
#                 lowest = v
#
#     if lowest == None:
#         lowest = blocks[0]
#
#     blocks.remove(lowest)
#
#     return lowest

def select_optimal(input, blocks):

    lowest = None

    for v in blocks:
        if (input < v):
            if lowest == None or v < lowest:
                lowest = v

    if lowest == None:
        lowest = blocks[0]

    blocks.remove(lowest)

    return lowest


def play_deceitful(blocks_naomi, blocks_ken):
    np = 0

    #blocks_naomi.sort(None, None, True)
    # blocks_naomi.sort()
    # blocks_ken.sort()
    #
    # random.shuffle(blocks_naomi)
    #
    # while len(blocks_naomi) > 0:
    #     bn = blocks_naomi.pop()
    #     bk = select_optimal(bn, blocks_ken)
    #
    #     #print bn, bk
    #
    #     if (bn > bk):
    #         np += 1


    while len(blocks_naomi) > 0:

        done = False

        for v in blocks_ken:
            for vn in blocks_naomi:
                if (v < vn):
                    bn = vn
                    bk = select_optimal(blocks_ken[len(blocks_ken) - 1] + 0.0000001, blocks_ken)

                    blocks_naomi.remove(bn)

                    print bn, bk
                    if (bn > bk):
                        np += 1

                    done = True

                    break
            if done:
                break

        if not done:
            return np




        # while len(blocks_naomi) > 0 and blocks_naomi[0] < blocks_ken[0]:
        #     bn = blocks_naomi[0]
        #     bk = select_optimal(blocks_ken[len(blocks_ken) - 1] - 0.0000001, blocks_ken)
        #
        #     blocks_naomi.remove(blocks_naomi[0])
        #
        #     print bn, bk
        #
        #     if (bn > bk):
        #         np += 1
        #
        # while len(blocks_naomi) > 0 and blocks_naomi[len(blocks_naomi) -1 ] > blocks_ken[len(blocks_ken) - 1]:
        #     bn = blocks_naomi[len(blocks_naomi) -1 ]
        #     bk = select_optimal(bn, blocks_ken)
        #
        #     blocks_naomi.remove(bn)
        #
        #     print bn, bk
        #
        #     if (bn > bk):
        #         np += 1

        # if len(blocks_naomi) > 0 and not (blocks_naomi[0] < blocks_ken[0] and blocks_naomi[len(blocks_naomi) -1 ] > blocks_ken[len(blocks_ken) - 1]):
        #     bn = blocks_naomi[0]
        #     bk = select_optimal2(blocks_ken[len(blocks_ken) - 1] - 0.0000001, blocks_ken)
        #
        #     blocks_naomi.remove(blocks_naomi[0])
        #
        #     print bn, bk
        #
        #     if (bn > bk):
        #         np += 1


        #
        #
    # while len(blocks_naomi) > 0 and blocks_naomi[0] < blocks_ken[0]:
    #     bn = blocks_naomi[0]
    #     bk = select_optimal(blocks_ken[len(blocks_ken) - 1] - 0.0000001, blocks_ken)
    #
    #     blocks_naomi.remove(blocks_naomi[0])
    #
    #     print bn, bk
    #
    #     if (bn > bk):
    #         np += 1
    #
    # while len(blocks_naomi) > 0 and blocks_naomi[0] > blocks_ken[0]:
    #     bn = blocks_naomi[0]
    #     bk = select_optimal(blocks_naomi[0], blocks_ken)
    #
    #     blocks_naomi.remove(blocks_naomi[0])
    #
    #     print bn, bk
    #
    #     if (bn > bk):
    #         np += 1


        # t_bn = blocks_naomi[0]
        # t_bk = blocks_ken[0]
        #
        # print t_bn, t_bk
        #
        # if t_bn < t_bk:
        #     bn = t_bn
        #     bk = select_optimal(blocks_ken[len(blocks_ken) - 1] - 0.0000001, blocks_ken)
        #
        #     blocks_naomi.remove(bn)
        # else:
        #     bn = t_bn
        #     bk = select_optimal(t_bn, blocks_ken)
        #
        #     blocks_naomi.remove(t_bn)
        #
        # print bn, bk
        #
        # if (bn > bk):
        #     np += 1

        # t_bn = blocks_naomi[len(blocks_naomi) -1]
        # t_bk = blocks_ken[len(blocks_naomi) -1]
        #
        # print t_bn, t_bk
        #
        # if (t_bn < t_bk):
        #     bn = blocks_naomi[0]
        #     bk = select_optimal(t_bk - 0.0000001, blocks_ken)
        #
        #     blocks_naomi.remove(bn)
        # else:
        #     bn = t_bn
        #     bk = select_optimal(t_bn, blocks_ken)
        #
        #     blocks_naomi.remove(t_bn)
        #
        # print bn, bk
        #
        # if (bn > bk):
        #     np += 1


    return np

def play_fair(blocks_naomi, blocks_ken):
    np = 0

    blocks_naomi.sort()
    blocks_ken.sort()

    while len(blocks_naomi) > 0:
        bn = blocks_naomi.pop()
        bk = select_optimal(bn, blocks_ken)

        #print bn, bk

        if (bn > bk):
            np += 1

    return np


def process_testcase(cn, f, fout):
    amount_blocks = int(f.readline())
    blocks_naomi = f.readline().strip().split(" ")
    blocks_ken = f.readline().strip().split(" ")

    for k, v in enumerate(blocks_naomi):
        blocks_naomi[k] = float(v)

    for k, v in enumerate(blocks_ken):
        blocks_ken[k] = float(v)

    blocks_naomi.sort()
    blocks_ken.sort()

    print blocks_naomi
    print blocks_ken
    print

    #if (cn == 4):
    #    for v in blocks_naomi:
    #        l = list(blocks_naomi).remove(v)

    #        for l in blocks_naomi:



    dec = 0

    #if (cn == 4):
    #    while dec != 8:
    dec = play_deceitful(list(blocks_naomi), list(blocks_ken))

            #print dec

    fair = play_fair(blocks_naomi, blocks_ken)

    fout.write("Case #"+str(cn)+": "+str(dec) + " " + str(fair)+"\n")

    print
    print "Case #"+str(cn)+": "+str(dec) + " " + str(fair)

    print

f = open("QualProblemC.in")
fout = open("QualProblemC.out", "w")

amount_testcases = int(f.readline())

for i in range(0, amount_testcases):
    process_testcase(i + 1, f, fout)