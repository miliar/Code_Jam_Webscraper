import bisect
outp = open("output", "w")
with open("input.in") as f:
    skip = True
    case = 0
    for l in f:
        if skip:
            skip = False
        else:
            case += 1
            N, K = map(int, l.split())
            occupied = []
            last_bests = None
            for k in range(K):
                best_min_ls = -1
                best_max_ls = -1
                best_s = -1
                for s in range(N):
                    if s not in occupied:
                        ls = 0
                        rs = 0
                        if occupied:
                            ls_ins = bisect.bisect_right(occupied, s)
                            if ls_ins > 0:
                                ls = (s-1)-occupied[ls_ins-1]
                            else:
                                # there are stores on the left of s
                                ls = s
                            rs_ins = bisect.bisect_right(occupied, s)
                            if len(occupied) > rs_ins:
                                # the next occupied store minus this store
                                rs = occupied[rs_ins]-(s+1)
                            else:
                                # there are no stores on the right of s
                                rs = N-(s+1)
                        else:
                            ls = s
                            rs = N-(s+1)
                        min_ls = min(ls, rs)
                        max_ls = max(ls, rs)
                        choose = False
                        if min_ls > best_min_ls:
                            choose = True
                        elif min_ls == best_min_ls and max_ls > best_max_ls:
                            choose = True
                        if choose:
                            best_s = s
                            best_min_ls = min_ls
                            best_max_ls = max_ls
                ins_index = bisect.bisect_left(occupied, best_s)
                occupied[ins_index:ins_index] = [best_s]
                last_bests = [best_max_ls, best_min_ls]
            print("Case #%d: %d %d" % (case, best_max_ls, best_min_ls))
            outp.write("Case #%d: %d %d\n" % (case, best_max_ls, best_min_ls))

            # break
