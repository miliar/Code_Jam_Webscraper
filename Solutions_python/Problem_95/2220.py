class tongues:
  
  def __init__(self):
    self.f_in = open('tongues.txt')
    self.f_out = open('tongues_out.txt', 'w')
    lines = int(self.f_in.readline())
    self.d = self.initDict()

    for i in range(lines):
       response = self.process_line()
       
       self.f_out.write("Case #%d: %s" % (i+1, response+'\n'))
	
  def initDict(self):
    d = {}
    input = ("ejp mysljylc kd kxveddknmc re jsicpdrysi", "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd", "de kr kd eoya kw aej tysr re ujdr lkgc jv")
    output = ("our language is impossible to understand","there are twenty six factorial possibilities", "so it is okay if you want to just give up")
    for i in range(3):
      inp = input[i]
      out = output[i]
      length = len(inp)
      for j in range(length):
        if not inp[j] in d:
          d[inp[j]]=out[j]
    d['z']='q'
    d['q']='z'
    return d
	
  def process_line(self):
    line = self.f_in.readline().rstrip()
    line_length=len(line)    
    outline = ''
	
    for i in range(line_length):      
      outline+= self.d[line[i]]      
    
    #print outline
    #self.f_out.write(outline+'\n')
    return outline
	  
if __name__ == "__main__":
   t = tongues()