import ProblemFileIO

NAOMI = 0
KEN = 1

CHEAT = 1
FAIR = 2

def main():
    filename = 'D-large'
    ProblemIO = ProblemFileIO.ProblemFileIO(filename, case_function)
    for (Naomi, Ken) in ProblemIO.case_generator():
        result = solve(Naomi, Ken)
        ProblemIO.write_result(result)

def case_function(file_object):
    N = ProblemFileIO.read_int(file_object)
    Naomi = ProblemFileIO.read_float_list(file_object, ' ')
    Ken = ProblemFileIO.read_float_list(file_object, ' ')
    return (Naomi, Ken)
            
def solve(Naomi, Ken):
    Naomi = list(Naomi)
    Ken = list(Ken)
    Naomi.sort()
    Ken.sort()
    (N_score_cheat, K_score_cheat) = play(Naomi[:], Ken[:], CHEAT)
    (N_score_fair, K_score_fair) = play(Naomi, Ken, FAIR)
    return '%d %d' %(N_score_cheat, N_score_fair)
    
def play(Naomi, Ken, strategy):
    N_score = 0
    K_score = 0
    N = len(Naomi)
    for i in xrange(N):
        if (Naomi[-1] < Ken[0]): # Naomi is dominated
            K_score += N - i
            break
        if (Ken[-1] < Naomi[0]):  # Ken is dominated
            N_score += N - i
            break
        if (strategy == CHEAT):
            (Naomi, Ken, winner) = cheat_strategy(Naomi, Ken)
        if (strategy == FAIR):
            (Naomi, Ken, winner) = fair_strategy(Naomi, Ken)
        if (NAOMI == winner):
            N_score += 1
        else:
            K_score += 1
    return (N_score, K_score)

def cheat_strategy(Naomi, Ken):
    smallest_ken = Ken[0]
    N_index = find_smallest_winner(smallest_ken, Naomi)
    if (N_index == None):
        winner = KEN
    else:
        winner = NAOMI
    del Naomi[N_index]
    del Ken[0]
    return (Naomi, Ken, winner)

def fair_strategy(Naomi, Ken):
    largest_Naomi = Naomi[-1]
    K_index = find_smallest_winner(largest_Naomi, Ken)
    if (K_index == None):
        del Ken[0]
        winner = NAOMI
    else:
        del Ken[K_index]
        winner = KEN
    del Naomi[-1]
    return (Naomi, Ken, winner)

def find_smallest_winner(value, sorted_player_list):
    for i in xrange(len(sorted_player_list)):
        if value < sorted_player_list[i]:
            return i
    return None

if __name__ == '__main__':
    main()