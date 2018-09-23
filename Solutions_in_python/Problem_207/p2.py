all_valid_moves = {
        "R": ["B","Y"],
        "B": ["R","Y"],
        "Y": ["R","B"],
        }

all_opts = ["R", "B", "Y"]

def find_cycle(opt, moves=[]):
    def valid_moves(opt, moves):
        if len(moves) == 0:
            return [x for x in all_opts if opt[x] > 0]
        curr = moves[-1]
        return [x for x in all_valid_moves[curr] if opt[x] > 0]
    this_solved = False
    if sum(opt.values()) == 0 and moves[0] in all_valid_moves[moves[-1]]:
        return moves, True
    for s in opt:
        if 2*opt[s] > sum(opt.values()):
            return [], False
    for move in valid_moves(opt, moves):
        opt[move] -= 1
        moves += [move]
        moves, solved = find_cycle(opt, moves)
        if not solved:
            moves = moves[:-1]
            opt[move] += 1
        else:
            return moves, True
    return moves, this_solved

def check_solution(soln, opt):
    fake_opt = {x: 0 for x in opt}
    for i in range(len(soln)):
        fake_opt[soln[i]] = fake_opt.get(soln[i], 0) + 1
        assert soln[i] in all_valid_moves[soln[i-1]]
    assert fake_opt == opt, str(fake_opt) + " : " + str(opt)  + " : " + soln

def simple_solve(opt):
    for s in opt:
        if 2*opt[s] > sum(opt.values()):
            return [], False

    sorted_keys = sorted(opt, key=lambda x: -opt[x])
    max_key = sorted_keys[0]

    other_sum = sum(opt.values()) - opt[max_key]
    triples = other_sum - opt[max_key]
    real_triples = "".join(sorted_keys)*triples

    duplet_1 = (max_key + sorted_keys[1])*(opt[sorted_keys[1]] - triples)
    duplet_2 = (max_key + sorted_keys[2])*(opt[sorted_keys[2]] - triples)
    return real_triples + duplet_1 + duplet_2, True


T = input()
response = []
for t in range(T):
    N, R, O, Y, G, B, V = map(int, raw_input().split())
    opt = {"R": R, "B": B, "Y": Y}
    opt_copy = {"R": R, "B": B, "Y": Y}
    moves, solved = simple_solve(opt)
    if solved:
        response.append("Case #" + str(t+1) + ": " + moves)
    else:
        response.append("Case #" + str(t+1) + ": IMPOSSIBLE")
print "\n".join(response)
