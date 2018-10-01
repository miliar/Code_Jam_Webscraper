import re
import pdb

def debug_print(items):
    result = ''
    for item in items:
        result += str(item) + ' '
    print result

def get_wp(games):
    played = 0.0
    won = 0.0
    for game in games:
        if game == '1':
            played += 1
            won += 1
        elif game == '0':
            played +=1
    return won/played

file = open('A-large.in')
source = file.read().split('\n')
file.close()

number_testcases = int(source[0])
source = source[1:-1]
test_cases = []
for part in range(0, number_testcases):
    n = int(source[0])
    lines = source[1:n+1]
    source = source[n+1:]
    test_cases.append(lines)

results = ''
case_number = 1
for case in test_cases:
    n = len(case)
    parts = [] 
    for i in range(0,n): #for team in teams
        #Get WP
        games = list(case[i])
        wp = get_wp(games)
        #Get owp
        owp = 0.0
        counter = 0.0
        for j in range(0, len(games)): #for game in games
            if games[j] != '.': #if they played them
                others_games = list(case[j])
                del others_games[i]
                owp += get_wp(others_games)
                counter +=1
        owp /= counter
        parts.append({'wp':wp, 'owp':owp})
    results += "Case #" + str(case_number) + ":\n" 
    for i in range(0,n): #for team in teams
        games = list(case[i])
        wp = parts[i]['wp']
        owp = parts[i]['owp']
        oowp = 0.0
        counter = 0.0
        for j in range(0,len(games)): #for game in games
            if games[j] != '.': #if they played them
                oowp += parts[j]['owp']
                counter += 1
        oowp /= counter       

        rpi = 0.25 * wp + 0.50 * owp + 0.25 * oowp
        #debug_print([wp, owp, oowp])
        results += str(rpi) + '\n'        
    
    case_number += 1

print results

out = open('results.out', 'w')
out.write(results)
out.close()

