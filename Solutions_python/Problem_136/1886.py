def checkOneGame(C,F,X):
    currentTime = 0.
    currentRate = 2.0
    mini = X/2.
    while ((currentTime+(C/currentRate)+X/(currentRate+F)) < mini):
      mini = currentTime+(C/currentRate) + X/(currentRate+F)
      currentTime = currentTime+(C/currentRate)
      currentRate += F
    return str(mini)

if __name__ == '__main__':
    numberOfGames = int(raw_input())
    for i in range(numberOfGames):
        datas = map(float, raw_input().split())
        print("Case #"+str(i+1)+": " + checkOneGame(datas[0], datas[1], datas[2]))
