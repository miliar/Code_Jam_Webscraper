import math


t = int(input())
for i in range(1, t + 1):
  group_amount, suklaapalat = [int(s) for s in  input().split(" ")];
  
  #data containers
  groups = [int(s) for s in  input().split(" ")];
  tulos = 0;
  if(suklaapalat == 2):
    jj = {0:0, 1:0}
    for n in groups:
      jj[n % suklaapalat] += 1;
    tulos = jj[0];
    tulos += jj[1] // 2;
    if(jj[1] % 2 != 0):
      tulos += 1;

    #print("ryhmät:{}".format(jj))

  if(suklaapalat == 3):
    jj = {0:0, 1:0, 2:0}
    for n in groups:
      jj[n % suklaapalat] += 1;
    tulos = jj[0];

    yks_menee_kahteen = min(jj[1], jj[2])
    tulos += yks_menee_kahteen;
    jj[1] -= yks_menee_kahteen;
    jj[2] -= yks_menee_kahteen;
    if(jj[1] > 0):
      tulos += jj[1] // 3
      if jj[1] % 3 != 0:
        tulos += 1;
    elif(jj[2] > 0):
      tulos += jj[2] // 3
      if jj[2] % 3 != 0:
        tulos += 1;

  if(suklaapalat == 4):
    jj = {0:0, 1:0, 2:0, 3:0}
    for n in groups:
      jj[n % suklaapalat] += 1;
    tulos = jj[0];

    yks_menee_kolmeen = min(jj[1], jj[3])
    tulos += yks_menee_kolmeen;
    jj[1] -= yks_menee_kolmeen;
    jj[3] -= yks_menee_kolmeen;

    kaks_menee_kahteen = jj[2] // 2;
    tulos += kaks_menee_kahteen;
    jj[2] -= kaks_menee_kahteen * 2;

    if(jj[1] > 0):
      yks_menee_kahteen = min(jj[1] // 2, jj[2])
      tulos += yks_menee_kahteen;
      jj[1] -= yks_menee_kahteen * 2;
      jj[2] -= yks_menee_kahteen;
      if(jj[1] > 0):
        tulos += jj[1] // 4
        if (jj[1] % 4 != 0) or jj[2] > 0:
          tulos += 1;
    elif(jj[3] > 0):
      if(jj[2] > 0):
        #yksi 2 jäljellä
        if(jj[3] > 1):
          tulos += 1;
          jj[3] -= 2;
          jj[2] -= 1;

      if(jj[3] > 0):
        tulos += jj[3] // 4
        if jj[3] % 4 != 0 or jj[2] > 0:
          tulos += 1;
    else:
      if(jj[2] > 0):
        tulos += 1;


    #print("ryhmät:{}".format(jj))


  #solve


  #laske tulos

  print("Case #{0:.0f}: {1:.0f}".format(i, tulos));









