import sys


def testResult( d, c, n, ns):
   total = int(n) * 3
   toRet = 0
   cont = 0
   for x in ns:
      if int(x) >= total - 2:
         toRet += 1
      elif int(c) > 0 and cont < int(c):
         if int(x) >= int(n) and int(x) + 4 >= total:
            toRet += 1
            cont += 1
   return toRet

a = open('input_large.in','r')

line = a.readline()
inp = []
while line:
   inp.append(line.strip())
   line = a.readline()

# 
# 
# 
# 
# 
# 


case = 0
for test in inp:
   i = 0
   notes = []
   for numb in test.split(' '):
      i += 1
      if i == 1:
         #NUMBER OF GOOGLER
	 dancers = numb
      elif i == 2:
         #NUMBER OF CONTESTED
	 contested = numb
      elif i == 3:
         #NUMBER TO TEST
	 note = numb
      else:
         #NOTES
         notes.append(numb)

      #print numb
   ret = 0
   ret = testResult(dancers, contested, note, notes)
   case += 1
   print "Case #%d: %d" % (case,ret)
   #print dancers, contested, note, notes ,ret





sys.exit("SAI")























###
# PRECISA DEIXAR LEXICOGRAFICAMENTE O MENOR VALOR, ONDE:
# UPPER CASE VEM ANTES DE LOWER
# HIFEN VEM ANTES DE QUALQUER LETRA
# ESPACOS VEM ANTES DO HIFEN
###

oneCol = []
allCol = []
a = open('music_input.in','r')

line = a.readline()
c = 0
while line:
	if c in [0,1]:
		if c == 0:
			total = line.strip()
		c = c + 1
		line = a.readline()
		pass
	if line.strip().isdigit():
		allCol.append(oneCol)
		oneCol = []
		line = a.readline()
		pass
	oneCol.append(line.strip())
	line = a.readline()
allCol.append(oneCol)

a.close()
# TEST CASE:
#allCol = [['abc','cd','de','efg'],['abc','abcd','cef']]
#print allCol
sys.exit
case = 0
for oneCol in allCol:
	musics = oneCol
	if len(musics) == 0:
		continue
	case += 1
	print "Case #%d:" % (case)
	#print "MUSICAS: ", musics
	for music in oneCol:
		#print "Musica: ", music
		it = 1
		start = 0
		findArr = []
		achado = False
		while not achado and it <= len(music):
			while (start + it) <= len(music):
				test = music[start:it+start]
				#print "-TEST", test
				getOut = False
				for musicToTest in musics:
					#print "ToTest: ", musicToTest
# ALTERACOES:
# NAO IMPORTA SE JA FOI ACHADO, PRECISA VARRER TUDO
					if musicToTest == music: # or achado == True:
						#print 'PASSEI',musicToTest, music
						nono=1
					elif getOut:
						#print 'ja achei antes'
						nono=1
					elif musicToTest.lower().find(test.lower()) >= 0:
						#print '-ACHEI ', musicToTest, music, test
						getOut = True
# ALTERACOES:
# FINDED PRECISA SER UM ARRAY PARA BUSCAR O MELHOR NO FINAL
						finded = test
						continue
				if getOut:
					#print "--ACHADO: ", finded
					nono=1
#				elif not achado:
				else:
					#print "+++EH ESSE!!!!!!", test
					sucesso = test
					findArr.append(test.upper())
					achado = True
				start += 1
			it += 1
			start = 0
		if not achado:
			print ':(' #, music
		else:
			#print '+++EH ESSE!!!!!"',sucesso
			#print "\"%s\"" % (sucesso.upper()) #, music
			print "\"%s\"" % (sorted(findArr)[0]) #, music
			#print sorted(findArr)


sys.exit()











queen = ['a','e','i','o','u','A','E','I','O','U']
nobody = ['y','Y']

c = 0
for i in x:
	c = c+1
	if i[-1] in queen:
		print "Case #%s: %s is ruled by a queen." % (c,i)
	elif i[-1] in nobody:
		print "Case #%s: %s is ruled by nobody." % (c,i)
	else:
		print "Case #%s: %s is ruled by a king." % (c,i)
