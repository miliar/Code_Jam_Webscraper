def load_data():
    with open("a-small.txt") as f:
        with open("answer.txt", 'w') as ans:
            T = int(f.readline().split()[0])
            for case in range(T):
                C, F, X = [float(i) for i in f.readline().split()]
                ans.write("Case #{}: {}\n".format(case + 1, solve_one(C, F, X)))


def solve_one(C, F, X):
    t_i = [0]
    res_i = [X / 2.0]
    i = 0
    continuer = True
    while continuer:
        t_i.append(C / (i * F + 2.0) + t_i[-1])
        i += 1
        res_i.append(X / (i * F + 2.0) + t_i[-1])
        continuer = res_i[-1] < res_i[-2]
    return res_i[-2]


def main():
    load_data()

if __name__ == "__main__":
    main()
