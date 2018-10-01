# Speaking in Tongues

# main code

fr = open('B-large.in', 'r')
fw = open('B-large.out', 'w')

numOfTestCase = int(fr.readline())

for x in range(0,numOfTestCase):
  result = ""
  print("========== Test case " + str(x+1) + " ==========")

  line = (fr.readline()).split(" ")
  N = int(line[0])
  S = int(line[1])
  p = int(line[2])

  from array import array
  scores = array('i')

  for i in range(3,N+3):
    scores.append(int(line[i]))

  # Sort the scores descending
  scores = sorted(scores, reverse=1)

  # Initialize the number of hi scorers and surprising credit
  numOfHiScorers = 0
  surprisingCredit = S

  for i in range(0,N):
    print("Analyzing " + str(scores[i]))

    currentScore = scores[i]
    
    # Set the normal total score limit and suprising score limit.
    if p > 1:
      normalScoreLimit = (p * 3) - 2
      surprisingScoreLimit = normalScoreLimit - 2
    elif p == 1:
      normalScoreLimit = (p * 3) - 2
      surprisingScoreLimit = 0 # Not applicable
    else:
      # p == 0
      # All Googlers should have score at least zero
      print("p = 0, Every Googlers should got p or more")
      numOfHiScorers = N
      break      

    # Decide whether he/she is part of hiscorers
    if currentScore >= normalScoreLimit:
      # for sure, he/she got at least one score p or higher
      print("Get at least one p score or higher")
      numOfHiScorers = numOfHiScorers + 1
    elif ((currentScore >= surprisingScoreLimit) and (p != 1)):
      # Need surprising credit to be possible he/she got the p score.
      # Not applicable if p == 1 because it is impossible to have score less than zero
      if surprisingCredit > 0:
        # Consume one credit, and add this person in the highscorer list
        print("Get at least one p, but with surprising scoring")
        surprisingCredit = surprisingCredit - 1
        numOfHiScorers = numOfHiScorers + 1
      else:
        # Surprising credit has been used up, this person is not possible to
        # get the p score
        print("No more surprising score possible, thus he/she is loser")
        # because the array is sorted, the rests would be the same
        # so, break the loop
        break
    else:
      # for sure, he/she didn't get higher than p
      print("Lower than p")
      # because the array is sorted, the rests would be the same
      # so, break the loop
      break

  result = str(numOfHiScorers)
  print ("Result :" + result)

  fw.write("Case #" + str(x+1) + ": " + result + "\n")

fr.close()
fw.close()
