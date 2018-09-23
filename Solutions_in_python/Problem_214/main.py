import itertools

def katso_risti(rivit, sarakkeet, talo):
  impossible = False;
  muutos = False;
  for r in range(rivit):
    for s in range(sarakkeet):
      if(talo[r][s] == "+"):
        #oikealle
        for s2 in range(s+1,sarakkeet,1):
          if(talo[r][s2] == "#"):
            #seinä
            break;
          if(talo[r][s2] == "+" or talo[r][s2] == "|"):
            talo[r][s] = "|";
            talo[r][s2] == "|";
            muutos = True;
            #print("Tämä");
          elif(talo[r][s2] == "-"):
            #IMPOSSIBLE!!
            impossible = True;
            pass;
        #vasen
        for s2 in range(s-1,-1,-1):
          if(talo[r][s2] == "#"):
            #seinä
            break;
          if(talo[r][s2] == "+" or talo[r][s2] == "|"):
            talo[r][s] = "|";
            talo[r][s2] == "|";
            muutos = True;
          elif(talo[r][s2] == "-"):
            #IMPOSSIBLE!!
            impossible = True;
            pass;
        #ylös
        for r2 in range(r+1,rivit,1):
          if(talo[r2][s] == "#"):
            #seinä
            break;
          if(talo[r2][s] == "+" or talo[r2][s] == "-"):
            talo[r2][s] = "-";
            talo[r2][s] == "-";
            muutos = True;
          elif(talo[r2][s] == "|"):
            #IMPOSSIBLE!!
            impossible = True;
            pass;
        #alas
        for r2 in range(r-1,-1,-1):
          if(talo[r2][s] == "#"):
            #seinä
            break;
          if(talo[r2][s] == "+" or talo[r2][s] == "-"):
            talo[r2][s] = "-";
            talo[r2][s] == "-";
            muutos = True;
          elif(talo[r2][s] == "|"):
            #IMPOSSIBLE!!
            impossible = True;
            pass;
      #print("talo: {}".format(talo));
      if(impossible):
        break;
    if(impossible):
      break;
  return (impossible, muutos);

def tarkasta(rivit, sarakkeet, talo):
  valmis = False
  for r in range(rivit):
    for s in range(sarakkeet):
      if(talo[r][s] == "+"):
        return False;
      if(talo[r][s] == "#"):
        continue;
      #tyhjä ruutu, osuuko joku?
      vaaka = 0;
      pysty = 0;
      #oikealle
      for s2 in range(s+1,sarakkeet,1):
        #print("oikelle [{}][{}]".format(r,s2))
        if(talo[r][s2] == "#"):
          #seinä
          break;
        if(talo[r][s2] == "-"):
          vaaka = 1
          break;
      #print("Oikean jälkeen vaaka={}".format(vaaka))
      #vasen
      for s2 in range(s-1,-1,-1):
        #print("vasen [{}][{}]".format(r,s2))
        if(talo[r][s2] == "#"):
          #seinä
          break;
        if(talo[r][s2] == "-"):
          vaaka = 1
          break;
      #print("Vasen jälkeen vaaka={}".format(vaaka))
      #ylös
      for r2 in range(r+1,rivit,1):
        if(talo[r2][s] == "#"):
          #seinä
          break;
        if(talo[r2][s] == "|"):
          pysty = 1
          break;
      #alas
      for r2 in range(r-1,-1,-1):
        if(talo[r2][s] == "#"):
          #seinä
          break;
        if(talo[r2][s] == "|"):
          pysty = 1
          break;

      if(talo[r][s] == '.'):
        if(vaaka == 0 and pysty == 0):
          return False;
      else: #ei saa osua
        if(vaaka != 0 or pysty != 0):
          return False;
  return True;

def korvaa_plussa_numeroin(rivit, sarakkeet, talo):
  i = 0;
  for r in range(rivit):
    for s in range(sarakkeet):
      if(talo[r][s] == "+"):
        #talo[r][s] = i;
        i += 1;
  return i;

def korvaa_plussa_listalla(rivit, sarakkeet, talo, joukko):
  result = [[] for s in range(rivit)]

  for r in range(rivit):
    result[r] = talo[r][:]

  i = 0;
  for r in range(rivit):
    for s in range(sarakkeet):
      if(result[r][s] == "+"):
        result[r][s] = joukko[i]
        i += 1;
  return result;


def katso_floors(rivit, sarakkeet, talo):
  impossible = False
  muutos = False;
  for r in range(rivit):
    for s in range(sarakkeet):
      if(talo[r][s] == '.'):
        #tyhjä ruutu, osuuko joku?
        vaaka = 0;
        pysty = 0;
        #oikealle
        for s2 in range(s+1,sarakkeet,1):
          #print("oikelle [{}][{}]".format(r,s2))
          if(talo[r][s2] == "#"):
            #seinä
            break;
          if(talo[r][s2] == "+" or talo[r][s2] == "-"):
            vaaka += 1
        #print("Oikean jälkeen vaaka={}".format(vaaka))
        #vasen
        for s2 in range(s-1,-1,-1):
          #print("vasen [{}][{}]".format(r,s2))
          if(talo[r][s2] == "#"):
            #seinä
            break;
          if(talo[r][s2] == "+" or talo[r][s2] == "-"):
            vaaka += 1
        #print("Vasen jälkeen vaaka={}".format(vaaka))
        #ylös
        for r2 in range(r+1,rivit,1):
          if(talo[r2][s] == "#"):
            #seinä
            break;
          if(talo[r2][s] == "+" or talo[r2][s] == "|"):
            pysty += 1
        #alas
        for r2 in range(r-1,-1,-1):
          if(talo[r2][s] == "#"):
            #seinä
            break;
          if(talo[r2][s] == "+" or talo[r2][s] == "|"):
            pysty += 1
        #talo[r][s] = (vaaka,pysty);
        if(pysty > 1):
          pysty = 0;
          #ei voi pystyyn ylös
          for r2 in range(r+1,rivit,1):
            if(talo[r2][s] == "#"):
              #seinä
              break;
            elif(talo[r2][s] == "+"):
              talo[r2][s] = "-"
              muutos = True;
            elif(talo[r2][s] == "|"):
              #IMPOSSIBLE!!
              impossible = True;
              pass;

          #ei voi pystyyn alas
          for r2 in range(r-1,-1,-1):
            if(talo[r2][s] == "#"):
              #seinä
              break;
            elif(talo[r2][s] == "+"):
              talo[r2][s] = "-"
              muutos = True;
            elif(talo[r2][s] == "|"):
              #IMPOSSIBLE!!
              impossible = True;
              pass;

        if(vaaka > 1):
          vaaka = 0;
          #ei voi vaakaan oikea
          for s2 in range(s+1,sarakkeet,1):
            if(talo[r][s2] == "#"):
              #seinä
              break;
            elif(talo[r][s2] == "+"):
              talo[r][s2] = "|"
              muutos = True;
            elif(talo[r][s2] == "-"):
              #IMPOSSIBLE!!
              impossible = True;
              pass;
          #ei voi vaakaan vasen
          for s2 in range(s-1,-1,-1):
            if(talo[r][s2] == "#"):
              #seinä
              break;
            elif(talo[r][s2] == "+"):
              talo[r][s2] = "|"
              muutos = True;
            elif(talo[r][s2] == "-"):
              #IMPOSSIBLE!!
              impossible = True;
              pass;
        if(vaaka == 0 and pysty == 0):
          #IMPOSSIBLE!!
          impossible = True;
          pass;
      if(impossible):
        break;
    if(impossible):
      break;
  return (impossible, muutos);

t = int(input())
for i in range(1, t + 1):
  rivit, sarakkeet = [int(s) for s in  input().split(" ")];
  
  talo = [[] for s in range(rivit)]

  for r in range(rivit):
    talo[r] = list(input());

  for r in range(rivit):
    for s in range(sarakkeet):
      if(talo[r][s] == '-' or talo[r][s] == '|'):
        talo[r][s] = "+"

  impossible = False;
  #print("Sarakkeet{} rivit{}".format(sarakkeet, rivit))
  #ratkaise

  muutos = True;
  while(muutos and not impossible):
    muutos = False;

    value = katso_floors(rivit, sarakkeet, talo);
    if(value[0]):
      impossible = True;
      break;
    muutos = muutos | value[1];

    value = katso_risti(rivit, sarakkeet, talo);
    if(value[0]):
      impossible = True;
      break;
    muutos = muutos | value[1];

    if(tarkasta(rivit, sarakkeet, talo)):
      #Valmis!!
      muutos = False;
      pass;

    if(tarkasta(rivit, sarakkeet, talo)):
      #print("Valmis");
      #print("talo: {}".format(talo));
      pass;
    else:
      #testaa eri permutaatiot plussilla:
      ratkomatta = korvaa_plussa_numeroin(rivit, sarakkeet, talo);
      valmis = False;
      #print("ratkomatta {}".format(ratkomatta));
      for joukko in itertools.product("-|",repeat = ratkomatta):
        #print("testaa {}".format(joukko))
        talo2 = korvaa_plussa_listalla(rivit, sarakkeet, talo, joukko);
        #print("talo2: {}".format(talo2));
        if(tarkasta(rivit, sarakkeet, talo2)):
          #print("talo2 rules!");
          valmis = True;
          talo = talo2;
          break;
      if(not valmis):
        impossible = True;

  tulos = -1;
  #laske tulos
  if(impossible):
    print("Case #{0:.0f}: IMPOSSIBLE".format(i));
  else:
    print("Case #{0:.0f}: POSSIBLE".format(i));
    for r in range(rivit):
      rivi = ""
      for s in range(sarakkeet):
        rivi += talo[r][s];
      print(rivi);








