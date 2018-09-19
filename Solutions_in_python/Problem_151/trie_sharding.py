#!/usr/bin/python

import sys
from pytrie import StringTrie as trie

def factorial( n ):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)

def cj_factorial( n ):
    if n == 0:
        return 1
    else:
        return (n*factorial(n-1))%1000000007


def nchoosek( n, k ):
    #return factorial(n)/(factorial(k)*factorial(n-k))
    answer = 1
    for i in range(1,k+1):
        answer *= (n - (k - i))
        answer /= i
    return answer


f = open( sys.argv[1] )

num_cases = int(f.readline().split()[0])

for i in range(num_cases):
    line = f.readline().strip()
    if len(line) <= 0:
        continue
    [num_strings, num_servers] = [int(x) for x in line.split()]
    strings = []
    for j in range(num_strings):
        strings.append( f.readline().strip() )
    #strings = {}
    #for j in range(num_strings):
        #strings[f.readline().strip()] = j

    #my_trie = trie( strings )
    #print my_trie._root.my_numkeys()

    max_nodes = 0
    max_count = 0
    # We can actually assume that the first word goes in the first server
    first_string = strings[0]
    strings = strings[1:]
    num_strings -= 1
    for j in range(num_servers**num_strings):
        placement_word = j
        servers = [{} for x in range(num_servers)]
        servers[0][first_string] = 0
        first_word = [-1 for x in range(num_servers)]
        first_word[0] = 0
        # put each word on a server
        for k in range(num_strings):
            #servers[j%num_servers].append( strings[k] )
            if not servers[placement_word%num_servers]:
                first_word[placement_word%num_servers] = k+1
            servers[placement_word%num_servers][strings[k]]=k+1
            placement_word = placement_word / num_servers
        # figure out if we're going to skip this iteration
        #print first_word
        bail = 0
        for k in range(num_servers-1):
            if first_word[k] > first_word[k+1]:
                bail = 1
        if bail:
            continue
        #print "Still going"
        total = 0
        for k in range(num_servers):
            my_trie = trie(servers[k])
            trie_size = my_trie._root.my_numkeys()
            if trie_size > 1:
                total += my_trie._root.my_numkeys()
        if total > max_nodes:
            max_count = 0
            max_nodes = total
        if total == max_nodes:
            max_count += 1
            max_count %= 1000000007
        #if total == 16:
            #print servers[0]
            #print servers[1]
            #print servers[2]
        #print servers[0]
        #print servers[1]
        #print total

    #print max_count, num_servers
    max_count = (max_count*cj_factorial(num_servers))

    print "Case #" + str(i+1) + ":", max_nodes, max_count

