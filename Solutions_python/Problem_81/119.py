cant = int(raw_input())
for t in range(cant):
  n = int(raw_input())
  jugados = []
  ganados = []
  wp = []
  vals = []
  for i in range(n):
    vals.append([])
    datos = raw_input()
    pj = 0
    pg = 0
    for j in range(len(datos)):
      if datos[j] == '.':
        vals[i].append(-1)
        continue
      pj += 1
      if datos[j] == '1':
        pg += 1
      vals[i].append(int(datos[j]))
    jugados.append(pj)
    ganados.append(pg) 
    wp.append(float(pg)/float(pj))

  owp = []
  for i in range(n):
    total = 0
    suma = 0
    for j in range(n):
      val = vals[i][j]
      if val >= 0:
        total += 1
        if val > 0:
          suma += float(ganados[j])/float(jugados[j]-1)
        else:
          suma += float(ganados[j]-1)/float(jugados[j]-1)
    owp.append(suma/float(total))

  oowp = []
  for i in range(n):
    total = 0
    suma = 0
    for j in range(n):
      val = vals[i][j]
      if val >= 0:
        total += 1
        suma += owp[j]
    oowp.append(suma/float(total)) 

  rpi = []
  for i in range(n):
    rpi.append(0.25 * wp[i] + 0.5 * owp[i] + 0.25 * oowp[i])

  print "Case #{0}:".format(t+1)
  for i in range(n):
    print rpi[i]
