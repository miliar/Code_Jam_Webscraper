import sys

f = open(sys.argv[1], "r")

cases = f.readline()

for case in range(int(cases)):

  blocks = int(f.readline())
  row = f.readline()
  naomi_blocks = list(row.strip().split())
  row = f.readline()
  ken_blocks = list(row.strip().split())

  #print "Naomi Blocks " , naomi_blocks
  #print "Ken Blocks " , ken_blocks

  naomi_blocks_sorted = sorted(naomi_blocks)
  ken_blocks_sorted = sorted(ken_blocks)

  #print "Naomi sorted blocks: " , naomi_blocks_sorted
  #print "Ken sorted blocks: " , ken_blocks_sorted

  naomi_points_war = 0
  naomi_points_des_war = 0

  #War Works
  for i in range(blocks):

    #naomi's choice and remove it
    choosen_naomi = float(naomi_blocks_sorted[0])
    naomi_blocks_sorted.pop(0)

    before_len = len(ken_blocks_sorted)
    for j in range(len(ken_blocks_sorted)):
      if (float(ken_blocks_sorted[j]) > choosen_naomi):
        ken_choosen = float(ken_blocks_sorted[j])
        ken_blocks_sorted.pop(j)
        break

    if (len(ken_blocks_sorted) == before_len):
      ken_choosen = float(ken_blocks_sorted.pop())

    if (choosen_naomi > ken_choosen):
      naomi_points_war = naomi_points_war + 1

  #War desceptive

  naomi_blocks_sorted = sorted(naomi_blocks)
  ken_blocks_sorted = sorted(ken_blocks)
  ken_blocks_sorted_reverse = ken_blocks_sorted[::-1]
  naomi_blocks_sorted_reverse = naomi_blocks_sorted[::-1]

  #print "Naomi blocks hight to low: ", naomi_blocks_sorted_reverse
  #print "Ken blocks high to low   : ", ken_blocks_sorted_reverse

  for i in range(blocks):

    #naomi's choice and remove it
    if (float(ken_blocks_sorted_reverse[0]) > float(naomi_blocks_sorted_reverse[0])):
      naomi_blocks_sorted[0] = float(ken_blocks_sorted_reverse[0]) - 0.00000001

    choosen_naomi = float(naomi_blocks_sorted_reverse[0])
    naomi_blocks_sorted_reverse.pop(0)

    before_len = len(ken_blocks_sorted_reverse)
    for j in range(len(ken_blocks_sorted_reverse)):
      if (float(ken_blocks_sorted_reverse[j]) < choosen_naomi):

        ken_choosen = float(ken_blocks_sorted_reverse[j])
        #print "J: ", j, "Ken Choosen: ", ken_choosen
        ken_blocks_sorted_reverse.pop(j)
        break

    if (len(ken_blocks_sorted_reverse) == before_len):
      ken_choosen = float(ken_blocks_sorted_reverse.pop())

    if (choosen_naomi > ken_choosen):
      naomi_points_des_war = naomi_points_des_war + 1

    #print "Choosen Naomi: " , choosen_naomi, " Choosen Ken: ", ken_choosen



  print "Case #" + str(case+1) + ":", naomi_points_des_war, naomi_points_war
