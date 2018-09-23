from  copy import copy
T = int(raw_input())

class Action:
    def __init__(self, type, x, y):
        self.type = type
        self.x = x
        self.y = y

def solve_r1_approch2(game, steps, o_pos):
    for i in range(N):
        if game[0][i] == ".":
            game[0][i] = "+"
            steps.append(Action("+", 0, i))
    game[N-1][0] = "x"
    steps.append(Action("x", N-1, 0))
    for i in range(1, N-1):
        game[N-1][i] = "+"
        steps.append(Action("+", N-1, i))

    diff = 0
    for i in range(1, N-1):
        if N - i == o_pos:
            diff = -1
        game[i][N-i+diff] = "x"
        steps.append(Action("x", i, N-i+diff))
    return steps


def solve_r1_approch1(game, steps):
    for i in range(N):
        if game[0][i] == ".":
            game[0][i] = "+"
            steps.append(Action("+", 0, i))

    game[N-1][1] = "o"
    steps.append(Action("o", N-1, 1))
    for i in range(2, N-1):
        game[N-1][i] = "+"
        steps.append(Action("+", N-1, i))

    for i in range(N-2):
        game[i+1][N-i-1] = "x"
        steps.append(Action("x", i+1, N-i-1))
    return steps

def solve_r1(game):
    steps = []
    x_pos = -1
    o_pos = -1
    for i in range(N):
        if game[0][i] == "x":
            x_pos = i
            break
        if game[0][i] == "o":
            o_pos = i
            break

    if x_pos > -1:
        game[0][x_pos] = "o"
        steps.append(Action("o", 0, x_pos))
        o_pos = x_pos

    if x_pos == -1 and o_pos == -1:
        o_pos = N - 1
        game[0][o_pos] = "o"
        steps.append(Action("o", 0, o_pos))

    if o_pos == 0:
        steps = solve_r1_approch1(game, steps)
    else:
        steps = solve_r1_approch2(game, steps, o_pos)

    score = get_score(game)
    return score, steps


def get_score(game):
    global N
    score = 0
    for i in range(N):
        for j in range(N):
            if game[i][j] == "x" or game[i][j] == "+":
                score += 1
            elif game[i][j] == "o":
                score += 2
    return score


def get_allowed_models(x, y, game, rows, cols, dig, dig_):
    models = []
    if game[x][y] == "o":
        models = ["o"]
    elif game[x][y] == ".":
        models = ["."]
        if "+" not in dig[x+y] and "+" not in dig_[x-y] and "o" not in dig[x+y] and "o" not in dig_[x-y]:
            models.append("+")
        if "x" not in rows[x] and "o" not in rows[x] and "x" not in cols[y] and "o" not in cols[y]:
            models.append("x")
        if len(models) == 3:
            models.append("o")
    elif game[x][y] == "x":
        models = ["x"]
        if "+" not in dig[x+y] and "+" not in dig_[x-y] and "o" not in dig[x+y] and "o" not in dig_[x-y]:
            models.append("o")
    elif game[x][y] == "+":
        models = ["+"]
        if "x" not in rows[x] and "o" not in rows[x] and "x" not in cols[y] and "o" not in cols[y]:
            models.append("o")
    return models


def deepcopy(something):
    if type(something) == list:
        new_list = list()
        for item in something:
            new_list.append(copy(item))
        return new_list
    else:
        new_dict = dict()
        for key in something:
            new_dict[key] = copy(something[key])
        return new_dict


def run(x, y, rows, cols, dig, dig_, prev_actions, game, score):
    global N, best_score, best_solution
    if best_score == max_score:
        return
    allowed_models = get_allowed_models(x, y, game, rows, cols, dig, dig_)

    for allowed_model in allowed_models:
        new_x = x
        new_y = y
        new_rows = deepcopy(rows)
        new_cols = deepcopy(cols)
        new_dig = deepcopy(dig)
        new_dig_ = deepcopy(dig_)
        new_prev_actions = copy(prev_actions)
        new_game = deepcopy(game)
        new_score = score

        if allowed_model == "o" and (new_game[x][y] == "+" or new_game[x][y] == "x"):
            new_score += 1
        elif allowed_model == "o" and new_game[x][y] == ".":
            new_score += 2
        elif (allowed_model == "+" or allowed_model == "x") and new_game[x][y] == ".":
            new_score += 1

        prev = new_game[x][y]
        new_game[x][y] = allowed_model
        # Remove old
        if prev != "." and prev != allowed_model:
            if new_rows[x][prev] > 1:
                new_rows[x][prev] -= 1
            else:
                del new_rows[x][prev]

            if new_cols[y][prev] > 1:
                new_cols[y][prev] -= 1
            else:
                del new_cols[y][prev]

            if new_dig[x+y][prev] > 1:
                new_dig[x+y][prev] -= 1
            else:
                del new_dig[x+y][prev]

            if new_dig_[x - y][prev] > 1:
                new_dig_[x - y][prev] -= 1
            else:
                del new_dig_[x - y][prev]

        # Add new
        if allowed_model != "." and prev != allowed_models:
            if allowed_model not in new_rows[x]:
                new_rows[x][allowed_model] = 0
            new_rows[x][allowed_model] += 1

            if allowed_model not in new_cols[y]:
                new_cols[y][allowed_model] = 0
            new_cols[y][allowed_model] += 1

            if allowed_model not in new_dig[x+y]:
                new_dig[x+y][allowed_model] = 0
            new_dig[x+y][allowed_model] += 1

            if allowed_model not in new_dig_[x-y]:
                new_dig_[x - y][allowed_model] = 0
            new_dig_[x - y][allowed_model] += 1

        if allowed_model != prev:
            new_prev_actions.append(Action(allowed_model, x, y))

        if max_score == new_score:
            best_score = new_score
            best_solution = new_prev_actions
            return

        if new_x + 1 < N:
            new_x += 1
            run(new_x, new_y, new_rows, new_cols, new_dig, new_dig_, new_prev_actions, new_game, new_score)
        else:
            if new_y + 1 < N:
                new_x = 0
                new_y += 1
                run(new_x, new_y, new_rows, new_cols, new_dig, new_dig_, new_prev_actions, new_game, new_score)
            else:
                # Completed
                if new_score > best_score:
                    best_score = new_score
                    best_solution = new_prev_actions

for case in range(1, T+1):
    N, M = map(int, raw_input().strip().split())
    best_solution = []

    # Create 2-D Array
    init_game = []
    for _ in range(N):
        init_game.append(["."]*N )

    # Load preset models
    for model in range(M):
        model_type, model_x, model_y = raw_input().strip().split()
        model_x = int(model_x) - 1
        model_y = int(model_y) - 1
        init_game[model_x][model_y] = model_type

    if N < 4:
        if N == 1:
            max_score = 2
        elif N == 2:
            max_score = 4
        else:
            max_score = 4 + (N-2) * 3

        rows = {}
        cols = {}
        dig = {}
        dig_ = {}
        for i in range(N):
            rows[i] = {}
            cols[i] = {}
            for j in range(N):
                dig[i+j] = {}
                dig_[i-j] = {}

        for x in range(N):
            for y in range(N):
                if init_game[x][y] != ".":
                    if init_game[x][y] not in rows[x]:
                        rows[x][init_game[x][y]] = 0
                    rows[x][init_game[x][y]] += 1

                    if init_game[x][y] not in cols[y]:
                        cols[y][init_game[x][y]] = 0
                    cols[y][init_game[x][y]] += 1

                    if init_game[x][y] not in dig[x+y]:
                        dig[x+y][init_game[x][y]] = 0
                    dig[x+y][init_game[x][y]] += 1

                    if init_game[x][y] not in dig_[x - y]:
                        dig_[x - y][init_game[x][y]] = 0
                    dig_[x - y][init_game[x][y]] += 1

        score = get_score(init_game)
        best_score = score
        run(0, 0, rows, cols, dig, dig_, [], init_game, score)
    else:
        best_score, best_solution = solve_r1(init_game)

    print "Case #{}: {} {}".format(case, best_score, len(best_solution))
    for action in best_solution:
        print "{} {} {}".format(action.type, action.x+1, action.y+1)