import sys

def main():
    T = int(sys.stdin.readline())
    for case in range(1,T+1):
        
        set1 = set()
        card_position = int(sys.stdin.readline()) - 1
        game = []
        for _ in range(4):
            tmp_line = sys.stdin.readline()
            line = tmp_line.split()
            game.append(map(int, line))
        #print game
        #print game[card_position]
        set1 = set(game[card_position])
        
        card_position = int(sys.stdin.readline()) - 1
        game = []
        for _ in range(4):
            tmp_line = sys.stdin.readline()
            line = tmp_line.split()
            game.append(map(int, line))
        #print game
        #print game[card_position]
        set2 = set(game[card_position])
        
        intersection = set1 & set2
        
        if len(intersection) == 0:
            print 'Case #%d: Volunteer cheated!' %(case)
        elif len(intersection) == 1:
            print 'Case #%d: %d' %(case, intersection.pop())
        elif len(intersection) > 1:
            print 'Case #%d: Bad magician!' %(case)
            
            
        
main()
