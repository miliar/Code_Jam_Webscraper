import sys

def worldcup_min_costs(P, M, round_prices):
    
    #print 'P', P, 'M', M, 'round_prices', round_prices
    
    price = round_prices[0][0]
    
    attending = []
    for round in range(P):
        attending = [[False] * 2**round] + attending
    
    #print attending
        
    for team_index in range(len(M)):
        team_misses = M[team_index]
        game_index = team_index/2
        cur_round = 0
        for i in range(team_misses):
            
            #print team_index, 'init cur_round', cur_round, 'game_index', game_index
            
            game_index /= 2
            cur_round += 1
                    
        while cur_round < P:
            
            #print team_index, 'cur_round', cur_round, 'game_index', game_index
            attending[cur_round][game_index] = True

            game_index /= 2
            cur_round += 1            
            
            #if game_index == 0:
            #    break
            
        
    #print attending
    
    count = 0
    for i in range(len(attending)):
        for j in range(len(attending[i])):
            if attending[i][j]:
                count += 1
    
    return count*price


if __name__ == '__main__':
    ntests = int(sys.stdin.readline())
    for i in range(1, ntests+1):
        P = int(sys.stdin.readline())
        M = map(int, sys.stdin.readline().strip().split())
        round_prices = []
        for j in range(P):
            round_prices.append(map(int, sys.stdin.readline().strip().split()))
        ans = worldcup_min_costs(P, M, round_prices)
        print 'Case #%s: %s' %  (i, ans)
