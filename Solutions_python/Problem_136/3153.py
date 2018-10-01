text_file = "C:\Users\Public\googlejamq.txt"

def main():
    f = open(text_file, 'r')
    games = f.readline()
    for game in range(0,int(games)):
        cookies = 0
        seconds = 0
        rate = 2
        data = f.readline().split()
        cost = float(data[0])
        boost = float(data[1])
        goal = float(data[2])
        while (goal/rate) > (cost/rate +goal/(rate+boost)):
            seconds = seconds + cost/rate
            rate = rate + boost
        seconds = seconds + goal/rate

        print "Case #%i: %f" % (game+1, seconds)

    
if __name__ == "__main__":
    main()
    
